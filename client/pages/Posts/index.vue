<template>
  <div>
    <h1>Posts list</h1>

    <div class="controllers">
      <div class="search">
        <input
          v-model.lazy="searchWord"
          @change="search"
          type="text"
          class="search__input"
          placeholder="Enter..."
        />
      </div>
      <div>
        <div class="line">
          <nuxt-link to="/posts/create/" class="btn btn__add_post"
            >Add post</nuxt-link
          >
        </div>
        <p>Index: {{ this.pageIndex }}</p>
        <div class="line">
          <button
            v-on:click="previousPosts"
            class="btn__pagination btn__pagination--previous"
          >
            &laquo;
          </button>
          <button
            v-on:click="nextPosts"
            class="btn__pagination btn__pagination--next"
          >
            &raquo;
          </button>
        </div>
      </div>
    </div>
    <div class="posts_list">
      <Post
        v-for="post in posts"
        :key="post.id"
        :id="post.id"
        :title="post.title.toUpperCase()"
        :content="post.content"
        :date="post.created_at"
      />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import Post from "./components/Post";

export default {
  components: {
    Post,
  },
  data() {
    return {
      posts: [],
      next: "",
      previous: "",
      pageIndex: 1,
      searchWord: "",
    };
  },
  async created() {
    let url = "http://localhost:8000/api/posts/?";
    console.log("here");
    this.getPosts(url);
  },
  computed: {},
  methods: {
    async nextPosts() {
      if (this.next) {
        await this.getPosts(this.next).then(() => {
          this.pageIndex++;
        });
      }
    },
    async previousPosts() {
      if (this.previous) {
        await this.getPosts(this.previous).then(() => {
          this.pageIndex--;
        });
      }
    },
    async search() {
      this.pageIndex = 1;
      this.getPosts();
    },
    async getPosts(url = "http://localhost:8000/api/posts/?") {
      const config = {
        headers: {
          Accept: "application/json",
        },
      };

      try {
        const res = await axios.get(url + "&q=" + this.searchWord, config);
        this.posts = res.data.results;
        this.next = res.data.links.next;
        this.previous = res.data.links.previous;
        console.log(res.data);
      } catch (err) {
        console.log(err);
      }
    },
  },
};
</script>

<style>
.btn__pagination {
  background: white;
  border: 1px solid black;
  height: 30px;
  width: 30px;
}
.btn__pagination:active {
  background: rgba(117, 58, 184, 0.295);
}

.btn__add_post {
  text-align: center;
}
</style>
