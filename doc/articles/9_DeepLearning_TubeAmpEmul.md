---


---

<h1 id="deep-learning-for-tube-amplifier-emulation">Deep Learning for Tube Amplifier Emulation</h1>
<p>Resume of the following article :<br>
<a href="https://arxiv.org/pdf/1811.00334.pdf">https://arxiv.org/pdf/1811.00334.pdf</a></p>
<h2 id="introduction">Introduction</h2>
<p><strong>Problematc :</strong><br>
Difficulties to reproduce analogic sounds.<br>
In this article the researchers tries to reproduce the effects from the Fender Bassman 56F-A vacuum-tube amplifier.</p>
<p>Two main approaches to virtual analog modeling :</p>
<ul>
<li>white-box modeling : circuit analysis and simulation (wave digital filters WDF) --&gt; high degree of accuracy</li>
<li>black-box modeling : based on input-output measurements of the device under study --&gt; general, less accurate, does not include oftenly user control.</li>
</ul>
<p>The idea in this paper is to overcome the limitations of a conventional black-box by using a deep neural network</p>
<h2 id="architecture">Architecture</h2>
<p>references about amplifier circuit here :<br>
<a href="https://pure.qub.ac.uk/portal/files/124498748/The_Fender_Bassman_5F6_A_Family_of_Preamplifier_Circuits_A_Wave_Digital_Filter_Case_Study.pdf">The Fender Bassman 5F6-A Family of Preamplifier Circuits—A Wave Digital Filter Case Study</a></p>
<p>This Neural Network is a variant of the WaveNet depp neural Network + SPICE model of the tube amplifier.</p>
<p><strong>WaveNet architecture :</strong><br>
2 main parts : a stack of dilated causal convolution layers (nonlinear filter bank) where the output of each conv layer is used as input to a fully connected post-processing module (fully-connected neural  network.</p>
<p><img src="https://www.i-programmer.info/images/stories/News/2018/Nov/A/fender1.jpg" alt=""></p>
<h2 id="results">Results</h2>

