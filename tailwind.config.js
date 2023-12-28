/** @type {import('tailwindcss').Config} */
export default {
  content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        'yellow': '#f7d938;',
        'black': '#000000;',
        'darkblue': '#161F27;',
        'gray': '#333333;',
        'grey': '#333333;',
      },
      fontFamily: {
        'sans': ['Open Sans', 'sans-serif'],
        'roboto': ['Roboto', 'sans-serif'],
        'kanit': ['Kanit', 'sans-serif'],
      },
      fontSize: {
        paragraph: '1.4rem;',
      },
      animation: {
        fadeup: 'fadeup 2s',
      },
      keyframes: {
        fadeup: {
          '0%': { transform: 'translateY(2rem) scale(.9)', opacity: 0},
          '100%': { transform: 'translateY(0px) scale(1)', opacity: 1},
        }
      }
    },
  },
  plugins: [
    /* Idk how plugins would be imported */
  ],
};
