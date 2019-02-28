---


---

<h1 id="neural-audio-synthesis-of-musical-notes-with-wavenet-autoencoders">Neural Audio Synthesis of Musical Notes with WaveNet Autoencoders</h1>
<p>Analysis and understanding of the Synthesis of Musical Notes using the following article :<br>
<strong><a href="https://arxiv.org/pdf/1704.01279.pdf">https://arxiv.org/pdf/1704.01279.pdf</a></strong></p>
<h2 id="contribution-">Contribution :</h2>
<ul>
<li>Nsynth : A dataSet containing around 280 000 audio extract of 1000 instruments played at every peach.</li>
<li>WaveNet : A conditional CNN Generating raw audio samples.</li>
</ul>
<h2 id="problematic-">Problematic :</h2>
<p>The idea is to modify the already existing WaveNet architecture by creating an autoencoder to remove the external condition, necessary to create a longer signal than shot-to-mid signal.</p>
<h2 id="notes-">Notes :</h2>
<p>TTS (vocoders), music generation(synthesizers)</p>
<p>synthesizers : pitch, velocity, filter parameters(tone, timbre, dynamic of sound)</p>
<p>(look at FM Synthesis and Granular Synthesis)</p>

