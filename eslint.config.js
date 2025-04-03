import pluginVue from 'eslint-plugin-vue'

export default [
    ...pluginVue.configs['flat/recommended'],
    {
        rules: {
            'vue/singleline-html-element-content-newline': 'off',
            'vue/multi-word-component-names': 'off',
            'vue/max-attributes-per-line': ['error', {
                'singleline': {'max': 5},
                'multiline': {'max': 1},
            }],
            'vue/max-len': ['error', {
                'code': 120,
                'template': 120,
                'tabWidth': 2,
                'comments': 80,
                'ignorePattern': '',
                'ignoreComments': false,
                'ignoreTrailingComments': false,
                'ignoreUrls': false,
                'ignoreStrings': false,
                'ignoreTemplateLiterals': false,
                'ignoreRegExpLiterals': false,
                'ignoreHTMLAttributeValues': false,
                'ignoreHTMLTextContents': false,
            }],
        },
    },
]