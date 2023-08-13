module.exports = {
  env: {
    node: true,
  },
  extends: ["eslint:recommended", "plugin:vue/vue3-recommended", "prettier"],
  rules: {
    // Override/add rules settings here
  },
  overrides: [
    {
      files: ["*.vue"],
      rules: {
        "vue/no-multiple-template-root": "off",
        "vue/require-default-prop": "off",
        // Add more overrides if needed
      },
    },
  ],
};
