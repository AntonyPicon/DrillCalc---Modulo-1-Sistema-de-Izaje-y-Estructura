/**
 * DrillCalc - Module 1: Hoisting System & Structure
 * Author: Antony Picon, Mechanical Engineer
 * Description: UI Rendering module for DOM manipulation.
 */
/**
 * UI Renderer for DrillCalc
 * Defines functions to update the DOM based on calculation results.
 */

export class UiRenderer {

    constructor() {
        // Cache DOM elements if needed, or select dynamic
    }

    /**
     * Formats a number with commas and decimals.
     * @param {number} num 
     * @param {number} decimals 
     */
    formatNumber(num, decimals = 2) {
        if (num === undefined || num === null) return '--';
        return num.toLocaleString('en-US', {
            minimumFractionDigits: decimals,
            maximumFractionDigits: decimals
        });
    }

    updateSafetyCard(fd, alertLevel) {
        const card = document.getElementById('safety-card');
        const valueEl = document.getElementById('fd-value');
        const statusEl = document.getElementById('fd-status');

        // Reset classes
        card.classList.remove('safe', 'caution', 'danger');

        // Add new class based on alert level (mapped to lowercase)
        const levelClass = alertLevel.toLowerCase();
        card.classList.add(levelClass);

        valueEl.textContent = this.formatNumber(fd, 2);

        // Translate status
        const statusMap = {
            'SAFE': 'OPERACIÓN SEGURA',
            'CAUTION': 'PRECAUCIÓN',
            'DANGER': 'PELIGRO CRÍTICO'
        };
        statusEl.textContent = statusMap[alertLevel] || alertLevel;
    }

    updateMetrics(data) {
        // Efficiency (show as percentage)
        const effPercent = data.efficiency * 100;
        document.getElementById('efficiency-value').textContent = this.formatNumber(effPercent, 1);

        document.getElementById('fast-line-value').textContent = this.formatNumber(data.fast_line_tension, 0);
        document.getElementById('dead-line-value').textContent = this.formatNumber(data.dead_line_load, 0);
    }

    updateDerrickLoad(data) {
        const element = document.getElementById('derrick-load-value');
        element.textContent = this.formatNumber(data.derrick_load, 0);

        const bar = document.getElementById('load-bar');

        // Reset to trigger animation
        bar.style.width = '0%';
        setTimeout(() => {
            bar.style.width = '75%';
        }, 100);
    }

    updateTonMileResult(tonMiles) {
        const element = document.getElementById('ton-mile-value');
        element.textContent = this.formatNumber(tonMiles, 2);

        // Add a small bounce animation
        element.style.transform = 'scale(1.1)';
        setTimeout(() => {
            element.style.transform = 'scale(1)';
        }, 200);
    }

    switchView(viewId, title) {
        // Toggle view containers
        document.querySelectorAll('.view').forEach(v => v.classList.remove('active'));
        document.getElementById(viewId).classList.add('active');

        // Toggle nav items
        document.querySelectorAll('.nav-item').forEach(item => {
            if (item.getAttribute('data-view') === viewId) {
                item.classList.add('active');
            } else {
                item.classList.remove('active');
            }
        });

        // Update header title
        document.getElementById('current-view-title').innerHTML = `${title.toUpperCase()} <span class="module-tag">MOD. 1</span>`;
    }

    clearErrors(formType = 'hoisting') {
        const errorId = formType === 'hoisting' ? 'form-error' : 'ton-mile-form-error';
        const el = document.getElementById(errorId);
        if (el) el.textContent = '';
    }

    showError(msg, formType = 'hoisting') {
        const errorId = formType === 'hoisting' ? 'form-error' : 'ton-mile-form-error';
        const el = document.getElementById(errorId);
        if (el) el.textContent = `⚠️ ${msg}`;
    }
}

