module.exports = {
  content: [
    './public/**/*.{html,js}',
    './src/**/*.{html,js,svelte}',
    './node_modules/tw-elements/dist/js/**/*.js'],
  plugins: [
    require('tw-elements/dist/plugin')
  ]
}