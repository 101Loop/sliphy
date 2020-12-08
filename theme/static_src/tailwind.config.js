// This is a minimal config.
// If you need the full config, get it from here:
// https://raw.githubusercontent.com/tailwindlabs/tailwindcss/v1/stubs/defaultConfig.stub.js
module.exports = {
  important: true,
  future: {},
  purge: [],
  theme: {
    // fontFamily: {
    //   display: ['Gilroy', 'sans-serif'],
    //   body: ['Graphik', 'sans-serif'],
    // },
    extend: {
      colors: {
        cyan: '#9cdbff',
      },
      margin: {
        '96': '24rem',
        '128': '32rem',
      },
    }
  },
  variants: {
    backgroundColor: ['responsive', 'hover', 'focus','active'],
    fontSize: ['responsive', 'hover']
  },
  plugins: [
      require('@tailwindcss/forms'),
    ]
}
