// In your main.js file
document.getElementById('convert-form').addEventListener('submit', async (e) => {
    e.preventDefault();
    
    const file = document.getElementById('image-input').files[0];
    if (!file) return;

    const reader = new FileReader();
    
    reader.onload = async (event) => {
        try {
            // Get clean base64 without data URL prefix
            const base64Data = event.target.result;
            
            // Verify image data
            if (!base64Data.startsWith('data:image/')) {
                throw new Error('Invalid image format');
            }
            
            const response = await fetch('http://localhost:5000/api/convert', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify({
                    image: base64Data,  // Send full data URL
                    framework: document.getElementById('framework-select').value
                })
            });

            // ... rest of your code ...
        } catch (error) {
            console.error('Error:', error);
            alert(`Conversion failed: ${error.message}`);
        }
    };
    
    reader.readAsDataURL(file);  // This creates proper data URL
});