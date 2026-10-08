document.addEventListener('DOMContentLoaded', () => {
    const analyzeBtn = document.getElementById('analyzeBtn');
    const newsInput = document.getElementById('newsInput');
    const loadingSection = document.getElementById('loading');
    const resultSection = document.getElementById('result');
    const predictionBox = document.getElementById('prediction');
    const confidenceText = document.getElementById('confidence');

    analyzeBtn.addEventListener('click', async () => {
        const text = newsInput.value.trim();

        if (!text) {
            alert('Please enter some text to analyze.');
            return;
        }

        // Hide result, show loading, disable button
        resultSection.classList.add('hidden');
        loadingSection.classList.remove('hidden');
        analyzeBtn.disabled = true;
        analyzeBtn.textContent = 'Analyzing...';
        analyzeBtn.setAttribute('aria-busy', 'true');

        try {
            // Make real API call to the Flask backend
            const response = await fetch('http://localhost:5000/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ text: text }),
            });

            if (!response.ok) {
                throw new Error('Failed to analyze the text. API returned status ' + response.status);
            }

            const data = await response.json();

            if (data.error) {
                throw new Error(data.error);
            }

            // Update UI with results
            loadingSection.classList.add('hidden');
            resultSection.classList.remove('hidden');
            analyzeBtn.disabled = false;
            analyzeBtn.textContent = 'Analyze Article';
            analyzeBtn.removeAttribute('aria-busy');

            // Reset classes
            predictionBox.className = 'prediction-box';

            if (data.is_real) {
                predictionBox.textContent = 'REAL NEWS';
                predictionBox.classList.add('real');
            } else {
                predictionBox.textContent = 'FAKE NEWS';
                predictionBox.classList.add('fake');
            }

            if (data.confidence && data.confidence > 0) {
                confidenceText.textContent = `Confidence Score: ${data.confidence}%`;
            } else {
                confidenceText.textContent = "";
            }

        } catch (error) {
            console.error('Error during analysis:', error);
            alert('An error occurred during analysis: ' + error.message);

            loadingSection.classList.add('hidden');
            analyzeBtn.disabled = false;
            analyzeBtn.textContent = 'Analyze Article';
            analyzeBtn.removeAttribute('aria-busy');
        }
    });
});
