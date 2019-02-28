---


---

<h1 id="neural-music-synthesis-for-flexible-timbre-control">Neural Music Synthesis for Flexible Timbre Control</h1>
<p>Analysis and understanding of the Synthesis of Music for Flexible Timbre Control using the following article :<br>
<strong><a href="https://arxiv.org/pdf/1811.00223.pdf">https://arxiv.org/pdf/1811.00223.pdf</a></strong></p>
<h2 id="problematic">Problematic</h2>
<p>Presentation of Mel2Mel, a flexible music synthesizer. It uses a learned non linear music instrument embedding such as timbre control parameters with a synthesis engine based on WaveNet. This synthetizer is effective to apply morphing between instruments.</p>
<p><strong>TImbre control</strong><br>
Usually, there is a compromise between the control of the timbre and the quality of a realistic sound. In this work, the researchers try to find a compromise, giving a flexibility while controling variety of realistic sounds.</p>
<h2 id="definitions">Definitions</h2>
<p><strong>timbre morphing</strong><br>
Gradual transition between two or more sounds. Numerical interpolation of parameters according to the synthesis model used. But morphing depends on the range of timbres  covered by the model, that can be limited. Thus a data-driven approach is led here, generalizable for all timbres in the dataset.</p>
<p><strong>Timbre spaces and embeddings</strong><br>
Using Multidimensional Scaling in psychoacoustic, Mel-frequency cepstral coefficients (MFCCs), descriptors of spectral envelop, hidden layer weights in  music content analysis. Recently, a variational autoencoder has been developped, generating monophonic audio for a particular timbre embetdding without considering the attack and the decay (does not consider temporal evolution)</p>
<h2 id="method">Method</h2>
<p>synthesizing music given note sequences and timbre. the note sequences are furnished using midi file representing a piano roll corresponding to note timing and velocity. Then, it’s encoded as a matrix.<br>
FiLM layers : multi-step process that shapes a piano roll into its Mel spectrogram.</p>

