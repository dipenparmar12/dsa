/* eslint-disable */
module.exports = {
  env: {
    browser: true,
    es2021: true,
  },
  extends: ['airbnb', 'prettier'],
  parserOptions: {
    ecmaFeatures: {
      jsx: true,
    },
    ecmaVersion: 'latest',
    sourceType: 'module',
  },
  plugins: ['prettier'],
  settings: {},
  rules: {
    'prettier/prettier': [
      'warn',
      {
        endOfLine: 'auto',
      },
    ],
    // 'no-undef': 1,
    'react/no-children-prop': 'warn',
    'no-case-declarations': 'warn',
    'no-unused-vars': 'off' /* 'warn' */,
    'react/no-unescaped-entities': 'off',
    'no-console': 'off',
    'import/first': 'off',
    'import/no-cycle': 'off',
    'react/prop-types': 'off',
    'react/display-name': 'off',
    'arrow-body-style': 'off',
    'prefer-arrow-callback': 'off',
    'react/button-has-type': 'off',
    'func-names': 'off',
    'no-unused-expressions': 'off',
    'no-param-reassign': 'warn',
    'react/function-component-definition': 'off',
    'linebreak-style': ['off'],
    'no-script-url': 'warn',
    'react/self-closing-comp': 'warn',
    'react/no-array-index-key': 'warn',
    'react/no-unstable-nested-components': 'warn',
    'no-unreachable': 'warn',
    'no-nested-ternary': 'warn',
    'react/destructuring-assignment': 'warn',
    'default-param-last': 'warn',
    camelcase: 'warn',
    eqeqeq: 'warn',
    'no-useless-escape': 'off',
    'import/order': 'warn',
    'no-underscore-dangle': 'warn',
    'no-empty': 'warn',
    'prefer-template': 'warn',
    'object-shorthand': 'warn',
    'no-shadow': 'warn',

    semi: 'error',
    'no-unused-vars': 'warn',
    'func-names': 'off',
    'no-underscore-dangle': 'off',
    'consistent-return': 'off',
    'jest/expect-expect': 'off',
    'security/detect-object-injection': 'off',
    'no-multiple-empty-lines': 'warn',
    'prefer-const': 'off',
    camelcase: 'off',
    'no-plusplus': 'off',
    'no-console': [
      'off',
      {
        devDependencies: ['development/**/*.js'],
      },
    ],
    'no-unused-expressions': [
      'off',
      {
        devDependencies: ['development/**/*.js'],
      },
    ],
    'import/no-extraneous-dependencies': [
      'warn',
      {
        devDependencies: ['development/**/*.js'],
      },
    ],
    indent: [
      'warn',
      2,
      {
        SwitchCase: 2,
      },
    ],
  },
}
