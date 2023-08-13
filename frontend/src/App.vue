<template>
  <nav class="navbar navbar-expand-lg navbar-dark bg-dark px-5">
    <strong class="navbar-brand text-white">IntegraSolutions</strong>
    <router-link class="text-white" to="/">Home</router-link> |
    <router-link class="text-white" to="/about">About</router-link>
  </nav>

  <router-view class="m-5"> </router-view>
</template>
