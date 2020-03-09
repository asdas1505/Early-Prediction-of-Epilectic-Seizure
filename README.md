# Early-Prediction-of-Epilectic-Seizure

**Dataset**: Epilepsy data has been taken from University of Bornn, germany. Dataset consist of 1D signals time series data. The complete
data consist of five sets (A to E), each containing 100 single channel instances. Set A consist of EEG signals recorded from healthy volunteers while they were in 
relaxed and awake state with eyes opened. Whereas, the EEG signals in set E were recorded only during seizure activity.

## Result: 
We were able to achieve the accuracy of 99.09%.

## Our Architecture

Input_1 (InputLayer) (None, 512, 1)
___
Conv1d_1 (Conv1D) (None, 24, 5, 3)
___
batch_normalization_1 ()
___
Activation('relu')
___

Conv1d_2 (Conv1D) (None, 16, 3, 2) 
___
batch_normalization_2 ()
___
Activation('relu')
___

Conv1d_3 (Conv1D) (None, 8, 3, 2) 
___
batch_normalization_3 ()
___
Activation('relu')
___
flatten_1 (Flatten)
___
dense_1 (Dense) (None, 20, activation="relu", kernel_initializer = "uniform") 
___
dense_2 (Dense) (None, 1, activation = 'sigmoid')



