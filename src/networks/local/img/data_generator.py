import numpy as np
import cv2
import global_values as gv

# LOADING THE BASELINE
print('[INFO] loading the baseline...')
baseline = cv2.imread('../../../data/base_quadrillage.png')


def generate_pict(nb_version_pict, folder, outline_value, pic_type):
    """ creates nb_pictures of pitch-lines and saves them permanently in the folder img_'folder'.
      Folder has to be a string and nb_pict is an integer."""

    # default values if pitches, thicknesses and/or colors don't change
    height = (3 % gv.NB_PITCH) * gv.LINE_WIDTH + (gv.LINE_WIDTH + 5) // 2
    thickness = 6
    sat = hue = val = 0
    # default indices
    pitch_ind = 0
    color_ind = 0

    # beginning value for thickness if there is a variation of thickness
    if pic_type[1] == 1:
        thickness = 12
    # tab of color values if there is a variation of colors
    hue_val_tab = [[(i * 180) / (gv.NB_COLOR // 2), 90] for i in range(gv.NB_COLOR // 2)] + \
                  [[(i * 180) / (gv.NB_COLOR // 2), 210] for i in range(gv.NB_COLOR // 2)]
    # tab of available thicknesses if there is a variation of thicknesses
    thickness_tab = [2, 7, 12]
    global_line_path = np.empty(gv.PICT_WIDTH, dtype=int)

    for i in range(nb_version_pict):

        # generation of lines path :
        outline = outline_value
        delta = (gv.LINE_WIDTH - (thickness * 2)) // 2 + outline
        variation = np.random.randint(0, delta - outline)  # the line begin at a random point in delta
        interval_max = np.random.randint(2, 50)  # interval allowed to keep the same height between each variation

        for l in range(gv.PICT_WIDTH):
            # to avoid a sharp variation, we keep the same variation height for each 'interval'
            interval = np.random.randint(1, interval_max)
            if l % interval == 0:  # if we want to change the height of the line
                tmp_var = np.random.randint(-1, 2)  # each variation is an increase or a decrease of 1 (or same height)
                if abs(variation + tmp_var) < delta:
                    variation = variation + tmp_var
                else:
                    variation = variation
            global_line_path[l] = gv.PICT_WIDTH + variation

        # pitch affiliation :
        for p in range(gv.NB_PITCH):
            if pic_type[0] == 1:
                pitch_ind = 69 + p  # 69 is pitch for la440
                height = p * gv.LINE_WIDTH + (gv.LINE_WIDTH + 5) // 2
            line_path = global_line_path - height - 1

            # generation of the pictures. There are nb_version_pict*NB_COLOR*NB_PITCH pictures :
            for m in range(gv.NB_COLOR):

                # creation of the baseline, quadrilled picture :
                line_image_rgb = baseline.copy()

                # color affiliation :
                line_image_hsv = cv2.cvtColor(line_image_rgb, cv2.COLOR_RGB2HSV)
                h, s, v = cv2.split(line_image_hsv)

                if pic_type[2] == 1:
                    color_ind = m
                    color = hue_val_tab[color_ind]
                    sat = 150
                    hue = color[0]
                    val = color[1]

                # thickness affiliation :
                for t in range(gv.NB_THICK):
                    thick_ind = t
                    thickness = thickness_tab[thick_ind]

                    for j in range(gv.PICT_WIDTH):

                        # creation of the line :
                        if 0 < line_path[j] < 400:
                            h[line_path[j]][gv.PICT_WIDTH - j - 1] = hue
                            s[line_path[j]][gv.PICT_WIDTH - j - 1] = sat
                            v[line_path[j]][gv.PICT_WIDTH - j - 1] = val

                            # and its thickness :
                        for k in range(thickness):
                            if 0 < line_path[j] - k < 400:
                                h[line_path[j] - k][gv.PICT_WIDTH - j - 1] = hue
                                s[line_path[j] - k][gv.PICT_WIDTH - j - 1] = sat
                                v[line_path[j] - k][gv.PICT_WIDTH - j - 1] = val

                            if 0 < line_path[j] + k < 400:
                                h[line_path[j] + k][gv.PICT_WIDTH - j - 1] = hue
                                s[line_path[j] + k][gv.PICT_WIDTH - j - 1] = sat
                                v[line_path[j] + k][gv.PICT_WIDTH - j - 1] = val

                    line_image_hsv = cv2.merge((h, s, v))
                    line_image = cv2.cvtColor(line_image_hsv, cv2.COLOR_HSV2RGB)

                    name = 'pitch' + str(pitch_ind) + '_thick' + str(thick_ind) + '_color' + str(color_ind) + '_' + str(
                        i) + '_' + folder + '.png'
                    print(name)

                    # save the picture in google colab :
                    cv2.imwrite('../../../data/bdd_img/img_' + folder + '/' + name, line_image)
