---


---

<h1 id="definitions">Definitions</h1>
<h2 id="gru">GRU</h2>
<p>GRU uses, so called, <strong>update gate and reset gate</strong>. Basically, these are two vectors which decide what information should be passed to the output. The special thing about them is that they can be trained to keep information from long ago, without washing it through time or remove information which is irrelevant to the prediction.</p>
<p><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/Gated_Recurrent_Unit%2C_type_2.svg/1280px-Gated_Recurrent_Unit%2C_type_2.svg.png" alt=""></p>
<h2 id="lstm">LSTM</h2>
<p>LSTMs are explicitly designed to <strong>avoid the long-term dependency problem</strong>. Remembering information for long periods of time is practically their default behavior, not something they struggle to learn!</p>
<p><img src="https://sds-platform-private.s3-us-east-2.amazonaws.com/uploads/32_blog_image_3.png" alt=""></p>

