<template>
  <sidebar>
    <div class="menu">
      <ul>
        <nuxt-link to="/posts"> <li>Posts</li></nuxt-link>
        <nuxt-link to="/auth/login"><li>Login</li></nuxt-link>
      </ul>
    </div>
  </sidebar>
</template>

<script>
export default {};
</script>

<style>
.menu {
  position: fixed;
  font-size: 2em;
}

li:hover {
  color: rgb(158, 107, 216);
  text-decoration: rgb(158, 107, 216);
}
</style>
