import torch

from image_transform import image_to_matrix

# might be slow for the first time
_model = torch.jit.load('model_example.pt')

# set model to eval mode
_model.eval()


def predict(
        images: list[list[list[list[float]]]],
) -> list[list[float]]:
    # convert features to tensor
    _features = torch.tensor(images)

    # do some prediction
    with torch.no_grad():
        prediction = _model(_features)

    # convert prediction to list
    return prediction.tolist()


if __name__ == '__main__':
    print(predict(torch.rand(1, 3, 32, 32).tolist()))
    with open('image_example.png', 'rb') as f:
        print(predict(image_to_matrix(f.read(), 32, 32)))
