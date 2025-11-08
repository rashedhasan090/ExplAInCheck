// ExplAInCheck Frontend Application
const API_BASE_URL = 'http://localhost:5000/api';

document.addEventListener('DOMContentLoaded', () => {
    const verifyBtn = document.getElementById('verify-btn');
    const demoBtn = document.getElementById('demo-btn');
    const explanationInput = document.getElementById('explanation-input');
    const resultsSection = document.getElementById('results-section');
    
    verifyBtn.addEventListener('click', async () => {
        const explanation = explanationInput.value.trim();
        const domain = document.getElementById('domain-select').value;
        
        if (!explanation) {
            alert('Please enter an explanation to verify.');
            return;
        }
        
        verifyBtn.disabled = true;
        verifyBtn.textContent = '⏳ Verifying...';
        
        try {
            const response = await fetch(`${API_BASE_URL}/verify`, {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({ explanation, domain })
            });
            
            const data = await response.json();
            displayResults(data);
        } catch (error) {
            alert('Error connecting to API. Using demo data.');
            displayDemoResults();
        } finally {
            verifyBtn.disabled = false;
            verifyBtn.textContent = '🔍 Verify Explanation';
        }
    });
    
    demoBtn.addEventListener('click', () => {
        const demoText = "You should water banana plants at 5pm because the soil is cooler, leading to less evaporation. Given that banana plants need consistent moisture, this timing maximizes water absorption.";
        explanationInput.value = demoText;
        displayDemoResults();
    });
});

function displayResults(data) {
    const resultsSection = document.getElementById('results-section');
    resultsSection.style.display = 'block';
    
    document.getElementById('overall-result').innerHTML = `
        <div class="score ${data.overall_score > 70 ? 'good' : 'warning'}">
            <strong>Verification Score:</strong> ${data.overall_score}%
        </div>
    `;
    
    document.getElementById('logical-structure').innerHTML = formatLogicalSteps(data.logical_steps);
    document.getElementById('issues-list').innerHTML = formatIssues(data.issues);
    document.getElementById('assumptions-list').innerHTML = formatAssumptions(data.assumptions);
    document.getElementById('verified-claims').innerHTML = formatClaims(data.verified_claims);
}

function displayDemoResults() {
    const demoData = {
        overall_score: 75,
        logical_steps: [
            {step: 1, content: "Water plants at 5pm", verified: true},
            {step: 2, content: "Cooler soil → less evaporation", verified: true}
        ],
        issues: [
            {type: "Missing Evidence", description: "No data on optimal watering time"}
        ],
        assumptions: ["Soil is cooler at 5pm", "Bananas need consistent moisture"],
        verified_claims: ["Evaporation is reduced in cooler conditions"]
    };
    displayResults(demoData);
}

function formatLogicalSteps(steps) {
    return steps.map(s => `<div>✅ ${s.content}</div>`).join('');
}

function formatIssues(issues) {
    return issues.map(i => `<div>⚠️ <strong>${i.type}:</strong> ${i.description}</div>`).join('');
}

function formatAssumptions(assumptions) {
    return assumptions.map(a => `<div>💡 ${a}</div>`).join('');
}

function formatClaims(claims) {
    return claims.map(c => `<div>✔️ ${c}</div>`).join('');
}
