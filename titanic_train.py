{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "b9e7a7ed",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.metrics import accuracy_score\n",
    "from sklearn.preprocessing import LabelEncoder"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "d51ec09a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting scikit-learn\n",
      "  Downloading scikit_learn-1.6.1-cp313-cp313-macosx_12_0_arm64.whl.metadata (31 kB)\n",
      "Requirement already satisfied: numpy>=1.19.5 in /opt/miniconda3/lib/python3.13/site-packages (from scikit-learn) (2.2.6)\n",
      "Collecting scipy>=1.6.0 (from scikit-learn)\n",
      "  Downloading scipy-1.15.3-cp313-cp313-macosx_12_0_arm64.whl.metadata (61 kB)\n",
      "Requirement already satisfied: joblib>=1.2.0 in /opt/miniconda3/lib/python3.13/site-packages (from scikit-learn) (1.5.0)\n",
      "Collecting threadpoolctl>=3.1.0 (from scikit-learn)\n",
      "  Using cached threadpoolctl-3.6.0-py3-none-any.whl.metadata (13 kB)\n",
      "Downloading scikit_learn-1.6.1-cp313-cp313-macosx_12_0_arm64.whl (11.1 MB)\n",
      "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m11.1/11.1 MB\u001b[0m \u001b[31m4.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0ma \u001b[36m0:00:01\u001b[0m\n",
      "\u001b[?25hDownloading scipy-1.15.3-cp313-cp313-macosx_12_0_arm64.whl (30.1 MB)\n",
      "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m30.1/30.1 MB\u001b[0m \u001b[31m4.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m00:01\u001b[0m00:01\u001b[0m\n",
      "\u001b[?25hUsing cached threadpoolctl-3.6.0-py3-none-any.whl (18 kB)\n",
      "Installing collected packages: threadpoolctl, scipy, scikit-learn\n",
      "Successfully installed scikit-learn-1.6.1 scipy-1.15.3 threadpoolctl-3.6.0\n"
     ]
    }
   ],
   "source": [
    "!pip install scikit-learn"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
