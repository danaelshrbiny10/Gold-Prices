# Egypt Gold Prices

The Egypt Gold Prices project is for people who want to know how much gold costs in Egypt every day. It looks at the prices in Egyptian money for each gram of gold. The aim is to help people, like investors and analysts, get a clear picture of what's happening with gold in Egypt. The project collects and keeps a record of daily gold prices, giving useful information about the Egyptian gold market. It's like a tool to understand how gold prices in Egypt relate to the global market.

![Dashboard](https://github.com/danaelshrbiny10/Gold-Prices/assets/54659424/7d5d3f58-d6fe-4b74-a61e-66ea9192c2af)


## Installation

To get started with the Gold Prices project:

1. Clone the repository to your local machine

```bash
git clone https://github.com/danaelshrbiny10/Gold-Prices.git
```

2. Create a virtual environment and activate it:

```bash
# install virtual enviroment
pip install virtualenv

# Create a virtual environment
virtualenv env

# Activate the virtual environment
source env/Scripts/activate
```

3. Install the project dependencies:

```bash
pip install -r requirements/base.txt
```

## Usage

You can use this [postman collection](https://www.postman.com/restless-space-444311/workspace/gold-prices/collection/13841690-e8e26385-362b-44e2-a0dd-68fa09c66b68?action=share&creator=13841690) to learn more about the API usage

## Dataset

The dataset containing daily gold prices in Egyptian pounds per gram. This dataset is available for download from [Kaggle](https://www.kaggle.com/datasets/mohamedmagdy11/egypt-gold-prices-daily-updated/).

## Getting Started

To get started with this project, follow these steps:

1. Download the dataset from [Kaggle](https://www.kaggle.com/datasets/mohamedmagdy11/egypt-gold-prices-daily-updated/).

2. Utilize data analysis tools like Python and libraries such as Pandas and Matplotlib to explore and visualize the data.

3. Gain valuable insights into the Egyptian gold market by studying historical pricing trends and patterns.

## run project

1- you can run it by using docker file

```bash
docker run -p 8888:8888 GoldPrices
```

You can use this [Jupyter tree](http://127.0.0.1:8888/tree) to learn more about the Main file.

## Contributors

- [**Yomna Tarek**](https://github.com/Yomnaelfiky4) `developer`
- [**dana elshrbiny**](https://github.com/danaelshrbiny10) `developer`

## License

This project is open-source and available under the [MIT License](LICENSE).
