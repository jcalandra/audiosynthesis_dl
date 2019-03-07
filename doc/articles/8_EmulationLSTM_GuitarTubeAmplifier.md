---


---

<h1 id="real-time-emulation-of-parametric-guitar-tube-amplifier-with-long-short-term-memory-neural-network">Real Time Emulation of Parametric Guitar Tube Amplifier with Long Short Term Memory Neural Network</h1>
<p>Resume of the following article :<br>
<a href="https://arxiv.org/pdf/1804.07145.pdf">https://arxiv.org/pdf/1804.07145.pdf</a></p>
<h2 id="introduction">Introduction</h2>
<p><strong>Problematic :</strong><br>
Musicians like  the sound of tube amplifiers as it sounds warmer and more dynamically than solid state (full transistors) amplifiers. However tube amplifiers are bulky, expensive and fragile. There is a need then to emulate these amplifiers. Some are already existing but not that much efficient and none are modelised using neural networks.<br>
This paper gives a proper emulation of the ENGL Retro Tube 50 amplifier in real time.</p>
<p><strong>Previous Researches :</strong></p>
<ul>
<li>Volterra series models (and its subclass)</li>
<li>Wiener-Hammerstein cascade models (HKISS)</li>
</ul>
<h2 id="architecture">Architecture</h2>
<p><strong>Data Set :</strong><br>
The input is a guitar signal of single notes and chords. A data set of 20sec is long enough to bring results. Normalisation of the data to make them fit the input of the LSTM.</p>
<p><strong>RNN :</strong><br>
nonlinearities change according to the input frequencies therefore it seems natural to take the previous values of the input signal x into account.</p>
<p><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSzH3p88x5wAeBLXziQvVQnllTmqi7qHyL3DEOmHUroKk5276Fy" alt=""><br>
pred is the signal that emulate the output signal of the amplifier and x is the input signal. to calculate the prediction pred[n] of the system, the RNN will need the last N values of the input signal.<br>
TO avoid the problem of Vanishing Gradient, LSTM cell is introduced, composed of 4 fully connected layers.</p>
<p><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS4_gIl9Oc4EPHDdue9Cm3Ui7Wbc1hJ_Y2b6WmQlHJPW41VrkpS3A" alt=""></p>
<p>g layer is the same as having a simple RNN cell, generating a candidiate vector for the cell state. The other layers are gate controllers ( f[n] = which part of the cell state is kept, i[n] = which part of the candidate should be added to the long term vector c, o[n] = part of the current state that should go to the output y[n]).<br>
y[n] is the output vector at time step n, which is not the prediction pred[n] of the input x[n].</p>
<h2 id="results">Results</h2>
<p>Less than 1% of Root Mean Square Error.</p>

