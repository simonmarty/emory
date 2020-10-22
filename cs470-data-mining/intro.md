# Intro

- Data: Collection of recorded facts
- Information: Patterns and structure underlying the data
- Knowledge: Organized and interconnected information that enables people to make decisions

## Process

* Data Collection
* Data formatting and cle3aning
* Data Visualization
* Modeling
* Model evaluation
* Model deployment

## Techniques

* Statistical analysis
* Association rule mining
* Machine learning
    - Supervised (classification)
    - Unsupervised (clustering)
* Graph analysis

# Lecture 2

## Typical Knowledge Extraction Workflow

World &rarr; *extraction* &rarr; Database &rarr; *cleanup* &rarr; Data warehouse &rarr; *selection and transformation* &rarr; ...

## Characteristics of Data Records

* **Dimensionality**: For computational reasons
* **Sparsity**: Can indicate the amount of information the data carries
* **Scale and resolution**: Algorithms and output patterns depend on data resolution
* **Distribution**: Can facilitate the design of algorithms

## Tag cloud and influence graph

Reason to use: visualize documents or graphs

## Similarity and Distance Metrics

Other than finding what data looks like, you also need to know how to do calculations  
Many models require you to compare data records

## Proximity measures for binary attributes

To compare two multi-dimensional binary data points.

# Lecture 3

## Metrics of data Quality
* Accuracy: correct or wrong
* Completeness
* Consistency
* Timeliness
* Believability
* Interpretability

## Major Tasks
* Data cleaning
  * Fill in missing values, smooth noisy data, identify or remove outliers, and resolve inconsistencies.
* Data integration
  * Integration of multiple databases or files
* Data reduction
  * Dimensionality

## Challenges in working with data
* Incomplete: lacking attribute values, lacking certain attributes of interest, or containing only aggregate data
* Noisy: Containing noise, errors, or outliers
* Inconsistent: containing discrepancies in codes or names
  * Age="42", Birthday="03/07/2010"
  * Was rating "1,2,3", now rating "A, B, C"
  * Discrepancy between duplicate records
* Intentional data distortion:
  * Jan. 1 as everyone's birthday?

## Handling missing values
* Ignore the tuple
* Fill in the missing value manually
* Fill it in automatically
  * Gloval constant
  * The attribute mean (for all samples belonging to the same class?)
  * The most probable value: inferece-based such as Bayesian formula or decision tree

* *f*(**x**)
* L(G(*f*))

## Handling noisy data

* Binning
  * First sort data and partition into (equal-frequency) bins
  * the one can smooth by bin means, smooth by bin median, smooth by bin boundaries, etc.
* Regression
  * Smooth by fitting the data into regression functions
* Clustering
  * Detect and remove outliers
* Combined computer and human inspection
  * Detect suspicious values and check by human (e.g., deal with possible outliers)

## Data Integration

* Combines data from multiple sources into a coherent store
* Reasons for conflicts in data
  * Having different representations
  * different scales
  * different names
* Forms of redundancy
  * Redundancy in objects: either in data records or attributes
  * Derived attributes: One attribute in a table might be derived from another set of attributes from another table (e.g. salary)

## Correlation Analysis (Nominal Data)

* Chi-square for measuring correlation between two categorical attributes
  * A has *c* values
  * B has *r* values
  * Write down the contingency table
    * o<sub>i,j</sub> is the number of instances with (A = a<sub>i</sub>, B = b<sub>j</sub>)
  * e<sub>i,j</sub> is the expected value in the cell (i,j)
  * *n* is the total number orf instances
* Correlated attributes have a high Chi-square value
* Correlation coefficient (Pearson's product) is used to measure the correlation between numerical data
* It is equivalent to standardized covariance

## Data Reduction Strategies

* Goal: Obtain a reduced representation of the data set that is much smaller in volume but yet

### Wavelet Transforms

* Project the vector X into Y
  * Both X and Y have the same dimensions
  * The dimensions of Y can be truncated with some loss in precision: the small values can gbe set to 0
  * The truncated vector is sparse and easier to handle
  * The inverse transform can be applied to approx. restore vector X
* This transformation can also be used to remove noise from data
* Pyramid algorithm
  * Length L must be an integer power of 2 (padding with 0s when necessary)
  * Each transform has 2 functions: smoothing, difference
  * Applies to pairs of data, resulting in two sets of data of length L/2
  * Applies two functions recursively until reaches the desired length

### Principal Component Analysis (PCA)

* Finds the projection that captures the largest amount of variation in data
  * Uses SVD decomposition