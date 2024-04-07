#        #          #                    In the name of God   #    #
#
#GitHub.com/cloner174
#cloner174.org@gmail.com
#
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, roc_auc_score, roc_curve

class LinkPrediction:
    @staticmethod
    def common_neighbors(graph, node1, node2):
        neighbors1 = set(graph[node1])
        neighbors2 = set(graph[node2])
        return len(neighbors1.intersection(neighbors2))

    @staticmethod
    def adamic_adar(graph, node1, node2):
        neighbors1 = set(graph[node1])
        neighbors2 = set(graph[node2])
        common_neighbors = neighbors1.intersection(neighbors2)
        score = 0
        for neighbor in common_neighbors:
            degree = len(graph[neighbor])
            score += 1 / np.log(degree) if degree > 1 else 0
        return score

    @staticmethod
    def resource_allocation(graph, node1, node2):
        neighbors1 = set(graph[node1])
        neighbors2 = set(graph[node2])
        common_neighbors = neighbors1.intersection(neighbors2)
        score = 0
        for neighbor in common_neighbors:
            degree = len(graph[neighbor])
            score += 1 / degree if degree > 0 else 0
        return score

    @staticmethod
    def preferred_attachment(graph, node1, node2):
        return len(graph[node1]) * len(graph[node2])

    @staticmethod
    def jaccard_coefficient(graph, node1, node2):
        neighbors1 = set(graph[node1])
        neighbors2 = set(graph[node2])
        intersection = len(neighbors1.intersection(neighbors2))
        union = len(neighbors1.union(neighbors2))
        return intersection / union if union != 0 else 0

    @staticmethod
    def cosine_similarity(graph, node1, node2):
        neighbors1 = set(graph[node1])
        neighbors2 = set(graph[node2])
        intersection = len(neighbors1 & neighbors2)
        norm1 = np.sqrt(len(neighbors1))
        norm2 = np.sqrt(len(neighbors2))
        if norm1 == 0 or norm2 == 0:
            return 0
        else:
            return intersection / (norm1 * norm2)

    @staticmethod
    def evaluate_model(X_train, X_test, y_train, y_test, model):
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        accuracy = accuracy_score(y_test, y_pred)
        roc_auc = roc_auc_score(y_test, y_pred)
        fpr, tpr, thresholds = roc_curve(y_test, y_pred)
        plt.figure(figsize=(8, 8))
        plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'ROC curve (AUC = {roc_auc:.2f})')
        plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title('Receiver Operating Characteristic (ROC) Curve')
        plt.legend(loc='lower right')
        plt.show()
        print(f" thresholds : {thresholds}")
        print(f"ROC AUC of {model.__class__.__name__}: {roc_auc:.2f}")
        print(f"Accuracy of {model.__class__.__name__}: {accuracy:.2f}")

    @staticmethod
    def train_model(graph, methods=['common_neighbors', 'adamic_adar',
                                    'resource_allocation', 'preferred_attachment',
                                    'jaccard_coefficient', 'cosine_similarity']):
        
        X, y = [], []
        for node1 in graph:
            for node2 in graph:
                if node1 != node2:
                    features = []
                    for method in methods:
                        features.append(getattr(LinkPrediction, method)(graph, node1, node2))
                    X.append(features)
                    y.append(1 if node2 in graph[node1] else 0)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        model = LogisticRegression()
        LinkPrediction.evaluate_model(X_train, X_test, y_train, y_test, model)
