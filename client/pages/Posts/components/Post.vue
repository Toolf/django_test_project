<template>
  <nuxt-link :to="'posts/' + id + '/'">
    <div class="post">
      <h3 class="post__title">{{ title }}</h3>
      <div class="line">
        <p class="post__content">{{ content.substring(0, 1000) }}...</p>
        <img
          style="margin: 20px"
          src="https://i.pinimg.com/236x/8e/ac/25/8eac255253320c19b79f6e85d0453466.jpg"
          alt=""
        />
      </div>
      <div class="line">
        <p class="post__date">{{ date.split("T")[0] }}</p>
      </div>
    </div>
  </nuxt-link>
</template>

<script>
export default {
  name: "Post",
  props: ["title", "id", "content", "date"],
};
</script>

<style>
.post {
  border-bottom: 2px solid rgb(158, 145, 190);
  padding: 5px 50px;
}

.post:hover {
  background-color: rgba(158, 86, 206, 0.233);
}

.post__title {
  font-size: 1.5em;
}

.post__date {
  font-weight: 100;
  text-align: right;
  padding: 0px 20px;
}
</style>
