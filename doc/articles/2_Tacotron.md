---


---

<h1 id="tacotron--towards-end-to-end-speech-synthesis">TACOTRON : Towards End-to-End Speech Synthesis</h1>
<p>Analysis and understanding of Tacotron architecture using the following article :<br>
<a href="https://arxiv.org/pdf/1703.10135.pdf">https://arxiv.org/pdf/1703.10135.pdf</a></p>
<h2 id="introduction-and-problematic">Introduction and Problematic</h2>
<p>A need for <strong>minimal human annotation</strong> : less laborious feature engineering + the adaptation to new data is easier.<br>
Preference for a <strong>single model</strong> over a multi-stage model as it avoid the accumulation of the error of each component.</p>
<p>Tacotron is based on <strong>seq2seq</strong> with <strong>attention paradigm</strong>.</p>
<h2 id="principle">Principle</h2>
<p>Tacotron takes characters as input and output raw spectrogram. With also audio as input, the initialisation can be random.</p>
<p><img src="https://pythonawesome.com/content/images/2018/09/Tacotron-pytorch.jpg" alt=""></p>
<p><strong>CBHG :</strong> a bank of 1-D convolutional filters, followed by highway networks (kind of LSTM) and a bidirectional gated recurrent unit recurrent neural network (GRU RNN).<br>
The input sequence is convolved by <strong>K sets of 1-D filters</strong>, where the k-th set contains C_{k} filters of width k. These filters model <strong>local and contextual information</strong>. The outputs are then stacked and max pooled. The processed sequence is put in <strong>few fixed-width 1-D convolutions</strong> that are added with the original input sequence.<br>
Then the convolution outputs are fed into a <strong>multi-layer highway network</strong> to extract <strong>high-level features</strong>. A <strong>bi-directionnal GRU RNN</strong> is stacked on top to extract the <strong>sequential features</strong> from forward and backward context.</p>
<blockquote>
<p>CBHG is a powerful module for extracting representations from sequences.</p>
</blockquote>
<p><strong>Encoder :</strong> The input is a character sequence, where each character is represented as a <strong>one-hot vector embedded</strong> into a continuous vector. Then non-linear transformations are applied to each embedding : a pre-net , wich is a <strong>bottleneck with dropout</strong>.  A CBHG module is put to at the output to give the final encoder to the attention module.</p>
<blockquote>
<p>The encoder aim to extract robust sequential representations of text.</p>
</blockquote>
<p><strong>Decoder :</strong> content based tanh attention decoder. the context vector and the attention RNN cell output are concatenated to form the input to the decoder RNNs (with GRUs). Conversion from seq2seq target to waveform using a post-processing network.</p>
<blockquote>
<p>reference to article 7</p>
</blockquote>
<h2 id="performances">Performances</h2>
<p>Tacotron produces a <strong>3.82 Mean Opinion Score</strong> (MOS).</p>

