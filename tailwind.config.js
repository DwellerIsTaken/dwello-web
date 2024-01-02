/** @type {import('tailwindcss').Config} */
export default {
  darkMode: 'class',
  content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        'yellow': '#f7d938;',
        'yhover': '#EBC90A;',
        'black': '#000000;',
        'footer': '#1C1C21;',
        'gray': '#6B6B71;',
        'grey': '#6B6B71;',
        'dark': '#161616;',
        'white': '#EFEFEF;',
        'discord': '#5965f2;',
        'blue': '#007BFF;',
        'placeholder': '#00000080;',
      },
      width: {
        'col': '40rem', //29.6rem
      },
      margin: {
        'footer': '40rem',
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
      },
    },
  },
  plugins: [
    /* Idk how plugins would be imported */
  ],
};
