/**
 * DrillCalc - Module 1: Hoisting System & Structure
 * Author: Antony Picon, Mechanical Engineer
 * Description: API client module for backend communication.
 */
/**
 * ApiClient for DrillCalc Module 1
 * Handles communication with the FastAPI backend.
 */
export class ApiClient {
    constructor(baseUrl = window.location.origin) {
        this.baseUrl = baseUrl;
    }


    /**
     * Sends calculation request to the backend.
     * @param {Object} inputData - The data collected from the form.
     * @returns {Promise<Object>} - The JSON response from the server.
     */
    async calculateHoisting(inputData) {
        const url = `${this.baseUrl}/module-1/calculate`;

        try {
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: JSON.stringify(inputData)
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || 'Error en la solicitud al servidor');
            }

            return await response.json();

        } catch (error) {
            console.error('API Error:', error);
            throw error;
        }
    }

    /**
     * Sends Ton-Mile calculation request to the backend.
     * @param {Object} inputData 
     * @returns {Promise<Object>}
     */
    async calculateTonMile(inputData) {
        const url = `${this.baseUrl}/module-1/calculate-ton-mile`;

        try {
            const response = await fetch(url, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json'
                },
                body: JSON.stringify(inputData)
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || 'Error en el cálculo de Ton-Mile');
            }

            return await response.json();

        } catch (error) {
            console.error('Ton-Mile API Error:', error);
            throw error;
        }
    }


    /**
     * Checks if the API is reachable.
     */
    async checkHealth() {
        try {
            const response = await fetch(`${this.baseUrl}/`);
            return response.ok;
        } catch (e) {
            return false;
        }
    }
}
