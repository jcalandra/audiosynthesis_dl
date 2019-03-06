---


---

<h1 id="samplernn-an-unconditional-end-to-end-neural-audio-generation-model">SampleRNN: An Unconditional End-To-End Neural AUdio Generation Model</h1>
<p>Analysis and understanding of SampleRNN architecture using the following article :<br>
<a href="https://arxiv.org/pdf/1612.07837.pdf">https://arxiv.org/pdf/1612.07837.pdf</a></p>
<h2 id="introduction">Introduction</h2>
<p>The idea is to create an unconditional audio generation model that generate one audio sample at a time.<br>
It consist in combining autoregressive multilayer perceptron with stateful recurrent neural networks.</p>
<p><strong>Contribution :</strong></p>
<ul>
<li>use of RNNs at different scales to model longer term dependencies in audio waveforms while training on short sequencies : memory efficiency during training.</li>
<li>comparison of variant models.</li>
<li>study and evaluate the impact of different componets of the model on three audio dataset and human evaluation.</li>
</ul>
<h2 id="samplernn-model">SampleRNN Model</h2>
<p>Organisation by hierarchy of modules, each operating at a different temporal resolution.<br>
<img src="http://deepsound.io/images/samplernn.png" alt="enter image description here"></p>
<p><strong>Frame-level module</strong></p>
<ul>
<li>higher-level modules : non-overlapping frames. Each frame-level module is a deep RNN which summarizes the history of its input into a vector for the next module.</li>
</ul>

