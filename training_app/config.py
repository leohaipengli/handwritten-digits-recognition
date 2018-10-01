class Config:
    # shape
    INPUT_SHAPE = (28, 28, 1)
    OUTPUT_CLASS = 10

    # model save
    SAVE_MODEL = True
    SAVE_MODEL_FILENAME = 'CS231N-handwritten-digits.h5'
    
    # checkpoint
    CHECKPOINT_FILEPATH = "weights-improvement-{epoch:02d}-{val_loss:.2f}.hdf5"

    # training
    LOSS = 'categorical_crossentropy'
    OPTIMIZER = 'adam'
    METRICS = ['accuracy']