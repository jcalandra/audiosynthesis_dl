---


---

<h1 id="wavenet--a-generative-model-for-raw-audio">WAVENET : A Generative Model For Raw Audio</h1>
<p>Analysis and understanding of WaveNet architecture using the following article :<br>
<a href="https://arxiv.org/pdf/1609.03499.pdf">https://arxiv.org/pdf/1609.03499.pdf</a></p>
<h2 id="introduction">Introduction</h2>
<p>In this paper, the Convolutional Neuronal Network used as product of conditional distributions WaveNet is presented. This WaveNet generates raw audio and is inspired by <strong>PixelRNN</strong>.<br>
The aim of this article was to find if there was the possibility to create such similar CNN as PixelRNN to generates audio speeches while these signal have really high temporal resolution (16000 samples/s). At the end, experiments, shows that WaveNet is far better than other TTS generator.</p>
<h2 id="wavenet">WaveNet</h2>
<p>WaveNet is a CNN taking in entry raw audio signals.<br>
<strong>WARNING :</strong> computing time very very long.<br>
<img src="https://raw.githubusercontent.com/buriburisuri/speech-to-text-wavenet/master/png/architecture.png" alt=""></p>
<blockquote>
<p>A traduire en anglais.</p>
</blockquote>
<p><strong>A generative Model of join probability</strong></p>
<p>La probabilité jointe p(x) est égale au produit (pour i allant de un au nombre de valeurs du signal sinusoidal) des probabilités de xi sachant tous les xj précédents. Ainsi, tous les extraits xi sont conditionnés selon les extraits de toutes les étapes précédentes. (voir schéma)</p>
<p><strong>Dilated Casual Convolution</strong><br>
Afin d’obtenir un receptive field plus grand (receptive field = nombre de neurones d’entrée nécessaires pour calculer le neurone de sortie), on processe a une convolution de dilation, c’est à dire qu’on « saute » des neurone des couches cachées intermédiaires.</p>
<p><strong>Softmax distributions</strong> : utilisation d’une loi mu pour quantifier de manière linéaire et reduire le nombre de valeur a calculer lors du calcul du softmax.</p>
<p><strong>Gated Activation Unit :</strong> combinaison plus complexe d’actvations (tanh et sigmoid)</p>
<p><strong>Residual and skip connexions :</strong> Un reseau bien complexe….</p>
<p><strong>Conditional WaveNet :</strong> si on ajoute une entrée h, on obtient la distribution p(x|h) égale au produit (pour i allant de un au nombre de valeurs du signal sinusoidal) des probabilités de xi sachant tous les xj précédents et sachant h.</p>
<p>Cette nouvelle entrée permet de donner des caractéristiques supplémentaires en entrée pour le son à produire (exemple, l’identité de qqn qui parle).</p>

