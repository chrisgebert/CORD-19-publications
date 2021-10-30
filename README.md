![get-latest-cord-19-publication-data](https://github.com/chrisgebert/CORD-19-publications/workflows/get-latest-cord-19-publication-data/badge.svg)

# CORD-19 Dataset Author Statistics

The CORD-19 dataset of COVID-19 publications is published weekly at [CORD-19 Historical Releases](https://ai2-semanticscholar-cord-19.s3-us-west-2.amazonaws.com/historical_releases.html). 

In order to understand the distribution of authors on papers in this dataset, this repository: 
- requests data from the latest published dataset, 
- calculates author statistics on publications in that dataset, 
- appends the latest statistics to the [data file](/data/CORD-19-historical-releases.csv)

| Author Statistics | Description |
| --- | --- |
| `Date` | Date of CORD-19 release |
| `Article Count` | Total number of articles in the dataset |
| `Mean Author Count` | Mean number of authors per paper |
| `Std Author Count` | Standard deviation of authors per paper |
| `Min Author Count` | Minimum number of author per paper in dataset |
| `25% Percentile` | 25% percentile of number of authors per paper in dataset |
| `50% Percentile` | 50% percentile of number of authors per paper in dataset |
| `75% Percentile` | 75% percentile of number of authors per paper in dataset |
| `Max Author Count` | Maximum number of authors per paper in dataset |


Inspired by: [https://github.com/canovasjm/covid-19-san-juan](https://github.com/canovasjm/covid-19-san-juan)
