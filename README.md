# Belgium Real Estate Price Predicition

## Objectives
- Create a prediction model whose unknown is the price of a property located in any commune of Belgium. 
- Get the most accurate model possible in other terms the lowest mean squared error possible.
- Implement an user interface to let anyone predict the price of a property. 

## Dataset description
- The training and test dataset comes from data scrapped by myself from the site [Immoweb](https://www.immoweb.be/) and [LogicImmo](https://www.logic-immo.be/).
### Shape 
- The dataset is initially composed of 60 000 entries and 17 features each.
#### Features list 
1. Locality : The locality where the property is situated.
2. Type of property : Either "house" or "appartment".
3. Price : A float number in euros.
4. Number of rooms : A float
5. Area : A float in square meter.
6. Fully equipped kitchen : A boolean either true or false.
7. Furnished : *Does the property come in with furniture ?* A boolean either true or false.
8. Open fire : *Does the property have an open fire ?* A boolean either true or false.
9. Terrace Area : A float number representing the size of the terrace in square meter. Is equal to 0.0 if the property has no terrace.
10. Garden Area : A float number representing the size of the garden in square meter. Is equal to 0.0 if the property has no garden.
11. Surface of the land : A float number representing th total surface of the property in square meter.
12. Number of facades : A float number representing the number of facades of the property.
13. Swimming pool : A boolean. Either true or false.
14. State of the building : Either 'medium', 'good', 'new', 'to renovate', regarding the state of the property.
15. Province : One of the ten Belgium provinces.
16. Region : One of the 3 Belgium region.
17. PriceperMeter : A float number in euros
 
## Data analysis

I tried to get some insights from the data before

## Data preprocessing

Some features needed to be transformed to be able to train and test our model with it. 
Here are the said transformation and the respective library used:

- One-Hot encoding the categorical columns => [One-Hot Encoder](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.OneHotEncoder.html)
- Scaling the numerical columns and the encoded categorical columns => [StandardSclaer](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html)
- Handle the missing data in the dataset => [SimpleImputer](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html)
