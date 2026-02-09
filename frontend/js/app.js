import { ApiClient } from './api_client.js';
import { UiRenderer } from './ui_renderer.js';

const api = new ApiClient();
const ui = new UiRenderer();

document.addEventListener('DOMContentLoaded', async () => {
    console.log('DrillCalc App Initialized');

    // Check API Status
    const statusEl = document.getElementById('api-status');
    const isOnline = await api.checkHealth();
    if (isOnline) {
        statusEl.textContent = 'API: ONLINE';
        statusEl.style.color = 'var(--status-safe)';
    } else {
        statusEl.textContent = 'API: OFFLINE';
        statusEl.style.color = 'var(--status-danger)';
    }

    // Handle Form Submit
    const form = document.getElementById('calc-form');
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        ui.clearErrors();

        // Gather Data
        const formData = new FormData(form);
        const inputData = {
            hook_load: parseFloat(formData.get('hook_load')),
            lines: parseInt(formData.get('lines')),
            sheaves: parseInt(formData.get('sheaves')),
            friction_factor: parseFloat(formData.get('friction_factor')),
            wire_strength: parseFloat(formData.get('wire_strength'))
        };

        // BasicClientSideValidation can happen here, but Schema handles it too.

        try {
            const results = await api.calculateHoisting(inputData);
            console.log('Results:', results);

            // Render Results
            ui.updateSafetyCard(results.safety_factor, results.alert_level);
            ui.updateMetrics(results);
            ui.updateDerrickLoad(results);

        } catch (error) {
            ui.showError(error.message);
        }
    });
});
