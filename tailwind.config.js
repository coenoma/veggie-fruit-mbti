/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./static/**/*.js"
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Nunito', 'sans-serif'],
      },
      colors: {
        primary: {
          50: '#fff7ed',
          100: '#ffedd5',
          200: '#fed7aa',
          300: '#fdba74',
          400: '#fb923c',
          500: '#f97316',
          600: '#ea580c',
          700: '#c2410c',
          800: '#9a3412',
          900: '#7c2d12',
        },
        pastel: {
          pink: '#ffd1dc',
          yellow: '#fff4bd',
          green: '#d0f0c0',
          blue: '#bde0fe',
        },
        background: {
          light: '#fff9f5',
          soft: '#fff0e6',
        }
      },
      borderRadius: {
        'xl': '1.5rem',
        '2xl': '2rem',
        '3xl': '3rem',
        'full': '9999px',
      },
      boxShadow: {
        'soft': '0 4px 12px -2px rgba(249, 115, 22, 0.1), 0 2px 6px -1px rgba(249, 115, 22, 0.06)',
        'hover': '0 10px 15px -3px rgba(249, 115, 22, 0.1), 0 4px 6px -2px rgba(249, 115, 22, 0.05)',
      },
      animation: {
        'fade-up': 'fadeUp 0.5s ease-out',
        'slide-in': 'slideIn 0.3s ease-out',
        'pulse-soft': 'pulseSoft 2s ease-in-out infinite',
      },
      keyframes: {
        fadeUp: {
          'from': { 
            opacity: '0',
            transform: 'translateY(20px)'
          },
          'to': { 
            opacity: '1',
            transform: 'translateY(0)'
          },
        },
        slideIn: {
          'from': { 
            opacity: '0',
            transform: 'translateX(-20px)'
          },
          'to': { 
            opacity: '1',
            transform: 'translateX(0)'
          },
        },
        pulseSoft: {
          '0%, 100%': {
            transform: 'scale(1)',
          },
          '50%': {
            transform: 'scale(1.05)',
          },
        },
      },
    },
  },
  plugins: [],
}
