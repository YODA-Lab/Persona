# Details

- **Data**: Dataset collected from participant interactions.
- **Persona-Predict1**: The Persona method using data from the first round to make predictions.
- **Persona-Predict2**: The Persona method utilizing data from the first two rounds for predictions.
- **Persona-Predict3**: The Persona method leveraging data from the first three rounds for predictions.
- **Persona-Predict4**: The Persona method using all data except the last round for predictions.
- **SBU**: An ablation study variant of the Persona method.
- **Generic**: Another ablation study variant of the Persona method.
- **HM1**: A baseline argumentation-based method for updating probability distributions of human models using argument graphs.
- **HM2**: An enhanced version of Hunter’s HM1 that incorporates argument structure to improve the update of probability distributions, used as another baseline.
  

For each folder, run the following command in the terminal to generate the results:

```js
bash automatic.sh
```
