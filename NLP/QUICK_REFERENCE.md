# NLP Quick Reference Guide 📚

## 🚀 Quick Navigation

### **Getting Started**
1. Read `README.md` - Overview and structure
2. Check `LEARNING_ROADMAP.md` - Detailed learning paths
3. Set up `Progress_Notes/learning_tracker.md` - Track your progress
4. Start with `01_Text_Preprocessing/` - Foundation skills

### **Learning Path Summary**
```
01_Text_Preprocessing → 02_Basic_NLP_Concepts → 03_Classification_Models
         ↓                        ↓                         ↓
04_Word_Embeddings → 05_Language_Models → 06_Advanced_Techniques
         ↓                        ↓                         ↓
07_Neural_Networks → 08_Sequence_Models → 09_Advanced_Projects
```

---

## 📖 Topic Quick Reference

### **01_Text_Preprocessing** 🧹
**What:** Clean and prepare text data
**Key Skills:** Tokenization, normalization, cleaning
**Time:** 2-3 days
**Next:** 02_Basic_NLP_Concepts

### **02_Basic_NLP_Concepts** 📊
**What:** Fundamental NLP operations and statistics
**Key Skills:** Word frequencies, string manipulation, NumPy
**Time:** 3-4 days
**Next:** 03_Classification_Models

### **03_Classification_Models** 🎯
**What:** Classify text into categories
**Key Skills:** Logistic regression, Naive Bayes, sentiment analysis
**Time:** 4-5 days
**Next:** 04_Word_Embeddings

### **04_Word_Embeddings** 🔤
**What:** Vector representations of words
**Key Skills:** CBOW, Skip-gram, embedding manipulation
**Time:** 5-6 days
**Next:** 05_Language_Models

### **05_Language_Models** 🗣️
**What:** Model and generate natural language
**Key Skills:** N-grams, vocabulary building, OOV handling
**Time:** 5-6 days
**Next:** 06_Advanced_Techniques

### **06_Advanced_Techniques** 🔬
**What:** Mathematical foundations and optimization
**Key Skills:** Linear algebra, PCA, vector operations
**Time:** 4-5 days
**Next:** 07_Neural_Networks

### **07_Neural_Networks** 🧠
**What:** Deep learning for NLP tasks
**Key Skills:** TensorFlow, Siamese networks, triplet loss
**Time:** 6-7 days
**Next:** 08_Sequence_Models

### **08_Sequence_Models** 📈
**What:** Process sequential text data
**Key Skills:** Hidden states, perplexity, sequence modeling
**Time:** 4-5 days
**Next:** 09_Advanced_Projects

### **09_Advanced_Projects** 🏆
**What:** Complete, integrated NLP applications
**Key Skills:** Project management, integration, evaluation
**Time:** 7-10 days
**Next:** Personal projects and specialization

---

## 🛠 Common Commands and Patterns

### **Text Preprocessing Checklist**
```python
# 1. Load and inspect text
# 2. Clean and normalize
# 3. Tokenize
# 4. Remove stop words (if needed)
# 5. Handle special characters
# 6. Convert to appropriate format
```

### **Classification Workflow**
```python
# 1. Preprocess text
# 2. Extract features (BoW, TF-IDF, embeddings)
# 3. Split train/validation/test
# 4. Train model
# 5. Evaluate performance
# 6. Tune hyperparameters
```

### **Word Embedding Pipeline**
```python
# 1. Prepare corpus
# 2. Build vocabulary
# 3. Train embeddings (or load pre-trained)
# 4. Evaluate embedding quality
# 5. Use for downstream tasks
```

---

## 📊 Performance Evaluation Quick Reference

### **Classification Metrics**
- **Accuracy:** Overall correctness
- **Precision:** True positives / (True positives + False positives)
- **Recall:** True positives / (True positives + False negatives)
- **F1-Score:** Harmonic mean of precision and recall

### **Language Model Metrics**
- **Perplexity:** How well model predicts next word (lower is better)
- **BLEU Score:** For translation quality
- **Cross-entropy:** Loss function for training

### **Embedding Evaluation**
- **Intrinsic:** Word similarity, analogy tasks
- **Extrinsic:** Performance on downstream tasks
- **Visualization:** t-SNE, PCA plots

---

## 🚨 Common Issues and Solutions

### **Memory Issues**
- Use batch processing for large datasets
- Consider data generators for training
- Monitor memory usage during embedding training

### **Performance Problems**
- Check data preprocessing quality
- Verify feature engineering steps
- Ensure proper train/validation splits
- Tune hyperparameters systematically

### **Code Organization**
- Keep preprocessing separate from modeling
- Use configuration files for parameters
- Implement proper error handling
- Write unit tests for key functions

---

## 📁 File Organization Tips

### **Notebook Naming Convention**
- `01_data_exploration.ipynb`
- `02_preprocessing.ipynb`
- `03_model_training.ipynb`
- `04_evaluation.ipynb`

### **Code Structure**
```
project/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── src/
│   ├── preprocessing.py
│   ├── models.py
│   └── utils.py
├── tests/
├── results/
└── README.md
```

---

## 🎯 Learning Tips

### **Daily Practice**
- Code for at least 30 minutes daily
- Keep a learning journal
- Experiment with different datasets
- Document interesting findings

### **Weekly Goals**
- Complete 1 topic per week (adjust based on complexity)
- Build small projects to reinforce learning
- Review and summarize key concepts
- Plan next week's learning objectives

### **Monthly Reviews**
- Assess progress against goals
- Identify knowledge gaps
- Plan advanced projects
- Update portfolio and resume

---

## 🔗 Quick Links

- **Main README:** `README.md`
- **Learning Path:** `LEARNING_ROADMAP.md`
- **Progress Tracker:** `Progress_Notes/learning_tracker.md`
- **Experiments:** `Personal_Experiments/README.md`
- **Portfolio:** `Project_Gallery/README.md`

---

## 🆘 Getting Help

1. **Check topic README** - Each folder has specific guidance
2. **Review your notes** - Look for similar challenges
3. **Try simpler examples** - Break down complex problems
4. **Search documentation** - TensorFlow, scikit-learn, etc.
5. **Community resources** - Stack Overflow, Reddit, Discord

**Remember: Every expert was once a beginner! 💪**
