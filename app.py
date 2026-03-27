{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "3538ff93-4745-463d-89af-145afd764ca6",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2026-03-27 15:06:51.857 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-27 15:06:52.267 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\LENOVO\\.conda\\envs\\ml\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2026-03-27 15:06:52.267 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-27 15:06:52.267 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-27 15:06:52.267 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-27 15:06:52.267 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-27 15:06:52.271 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-27 15:06:52.271 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-27 15:06:52.273 Session state does not function when running a script without `streamlit run`\n",
      "2026-03-27 15:06:52.273 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-27 15:06:52.273 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-27 15:06:52.273 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-27 15:06:52.273 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-27 15:06:52.273 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-27 15:06:52.273 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-27 15:06:52.278 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-27 15:06:52.278 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-27 15:06:52.280 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pickle\n",
    "import re\n",
    "\n",
    "# Load model and vectorizer\n",
    "model = pickle.load(open('model.pkl', 'rb'))\n",
    "vectorizer = pickle.load(open('vectorizer.pkl', 'rb'))\n",
    "\n",
    "# Cleaning function\n",
    "def clean_text(text):\n",
    "    text = text.lower()\n",
    "    text = re.sub(r'http\\S+', '', text)\n",
    "    text = re.sub(r'@\\w+', '', text)\n",
    "    text = re.sub(r'#', '', text)\n",
    "    text = re.sub(r'[^a-zA-Z\\s]', '', text)\n",
    "    return text\n",
    "\n",
    "# UI\n",
    "st.title(\"Twitter Sentiment Analysis\")\n",
    "\n",
    "user_input = st.text_area(\"Enter a tweet:\")\n",
    "\n",
    "if st.button(\"Predict\"):\n",
    "    cleaned = clean_text(user_input)\n",
    "    vectorized = vectorizer.transform([cleaned])\n",
    "    prediction = model.predict(vectorized)\n",
    "\n",
    "    if prediction[0] == 1:\n",
    "        st.success(\"Positive Sentiment 😊\")\n",
    "    else:\n",
    "        st.error(\"Negative Sentiment 😡\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "68d90971-1f7f-4775-8f4c-50d4ba903bd6",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:.conda-ml]",
   "language": "python",
   "name": "conda-env-.conda-ml-py"
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
   "version": "3.11.14"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
