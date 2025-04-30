# decode-algebraic-codes
This repository contains the code files of the study presented in our paper "A Low-Complexity Algorithm to Globally Recover Algebraic Codes over Finite Fields".

We attempt to decode algebraic codes over finite fields by combining classical algebraic techniques with structure-imposed neural networks. The project addresses both local recovery and global reconstruction of codewords transmitted over noisy or lossy channels.

![architecture](https://github.com/user-attachments/assets/ef7845c3-d084-496a-9f76-a1b893616a7a)

### Preliminary Experiments
These notebooks were used to understand and validate DFT/DCT behavior before imposing structure on the networks. 
- [Classical DCT2 and DCT3](https://github.com/oshani-jayawardane/decode-algebraic-codes/blob/main/1_Classical_DCT.ipynb)
- [Classical DFT and IDFT](https://github.com/oshani-jayawardane/decode-algebraic-codes/blob/main/2_Classical_DFT.ipynb)
- [DFT and DCT Relationship](https://github.com/oshani-jayawardane/decode-algebraic-codes/blob/main/4_DFT_DCT_Relationship.ipynb)

### Proposed FFT-like Algorithm
We propose a Classical FFT-like algorithm for the local recovery of codewords. We also test it as a benchmark for global recovery.
- [Classical FFT-Like Algorithm for Local Recovery](https://github.com/oshani-jayawardane/decode-algebraic-codes/blob/main/3_Classical_Algorithm.ipynb)
- [Classical FFT-Like Algorithm for Global Recovery](https://github.com/oshani-jayawardane/decode-algebraic-codes/blob/main/9_Classical_Algorithm_global_recovery.ipynb)

### Proposed DCT-III Structure-imposed Neural Network (StNN)
We propose a DCT-III structure-imposed neural network for global recovery of codewords. We train the model with clean training data and also with training data with 4%-6% Gaussian noise injected during each batch. 
- [DCT-StNN trained without noise](https://github.com/oshani-jayawardane/decode-algebraic-codes/blob/main/7_DCT3_StNN_genmatrix_encoded.ipynb)
- [DCT-StNN trained with noise injected](https://github.com/oshani-jayawardane/decode-algebraic-codes/blob/main/8_DCT3_StNN_genmatrix_encoded_data_with_noise.ipynb)

### Benchmark Algorithms
We compare performance of our proposed model with a Simple Feedforward Network (ANN) and a IDFT structure-imposed neural network
- [ANN](https://github.com/oshani-jayawardane/decode-algebraic-codes/blob/main/5_ANN_genmatrix_encoded.ipynb)
- [IDFT-StNN](https://github.com/oshani-jayawardane/decode-algebraic-codes/blob/main/6_IDFT_StNN_genmatrix_encoded.ipynb)
