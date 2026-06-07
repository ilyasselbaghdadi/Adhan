import tensorflow as tf
(x_train,y_train),(x_test,y_test) = tf.keras.datasets.cifar10.load_data()
x_train = x_train/255.0
x_test = x_test/255.0
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(16, (3,3), padding="same", activation='relu', input_shape=(32,32,3)), #type: ignore
    tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(32,32,3)), #type:ignore
    tf.keras.layers.MaxPooling2D((2,2)),

    tf.keras.layers.Conv2D(64, (3,3), padding="same", activation='relu', input_shape=(32,32,3)), #type:ignore
    tf.keras.layers.MaxPooling2D((2,2)),

    tf.keras.layers.Conv2D(128, (3,3), padding ="same", activation='relu', input_shape=(32,32,3)), #type:ignore
    tf.keras.layers.MaxPooling2D((2,2)),
    tf.keras.layers.Conv2D(256, (3,3), activation='relu', input_shape=(32,32,3)), #type:ignore
    tf.keras.layers.MaxPooling2D((2,2)),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(256, activation="relu"),
    tf.keras.layers.Dense(10, activation='softmax')
])
model.compile(
    optimizer='adam',
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)
x_train = x_train.reshape(-1,32,32,3)
x_test = x_test.reshape(-1,32,32,3)
model.fit(x_train,y_train,epochs=5)
test_loss, test_acc = model.evaluate(x_test, y_test)

print("Test accuracy:", test_acc)
