# Screenshot_to_Code

screenshot-to-code/
├── backend/
│   ├── app.py                 # Main Flask application
│   ├── requirements.txt       # Python dependencies
│   ├── .env                   # Environment variables
│   └── utils/
│       ├── __init__.py
│       ├── ocr.py            # Tesseract OCR functions
│       └── code_generator.py  # Groq API integration
├── frontend/
│   ├── public/
│   │   ├── index.html
│   │   └── favicon.ico
│   ├── src/
│   │   ├── components/
│   │   │   ├── ImageUpload.jsx
│   │   │   ├── CodeDisplay.jsx
│   │   │   └── LoadingSpinner.jsx
│   │   ├── App.jsx
│   │   ├── index.js
│   │   └── styles/
│   │       └── tailwind.css
│   ├── package.json
│   └── tailwind.config.js
├── README.md
└── start.sh                   # Script to run both services
