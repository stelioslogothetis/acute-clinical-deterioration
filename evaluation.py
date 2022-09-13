import pandas as pd
from IPython.display import display
import matplotlib.pyplot as plt

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    roc_auc_score,
    f1_score,
    fbeta_score,
    make_scorer,
    precision_recall_curve,
    ConfusionMatrixDisplay,
)

f2_score = make_scorer(fbeta_score, beta=2)

METRICS = {
    "Accuracy": "accuracy",
    "Precision": "precision",
    "Recall": "recall",
    "AUC": "roc_auc",
    "F1 Score": "f1",
    "F2 Score": f2_score,
}

def evaluate_from_pred(y_true, y_pred, y_pred_proba):
    display(
        pd.DataFrame(
            {
                "Accuracy": accuracy_score(y_true, y_pred),
                "Precision": precision_score(y_true, y_pred),
                "Recall": recall_score(y_true, y_pred),
                "AUC": roc_auc_score(y_true, y_pred_proba[:, 1]),
                "F1 Score": f1_score(y_true, y_pred),
                "F2 Score": fbeta_score(y_true, y_pred, beta=2),
            },
            index=["Model"],
        )
    )

    fig, ax = plt.subplots(1, 1, figsize=(5, 5))
    ax.grid(False)
    ConfusionMatrixDisplay.from_predictions(y_true, y_pred, ax=ax)



def evaluate(model, X, y):
    y_pred = model.predict(X)
    y_pred_proba = model.predict_proba(X)

    evaluate_from_pred(y, y_pred, y_pred_proba)
