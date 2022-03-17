<template>
  <div>
    <h1>Frontend Docker Compose POC</h1>
    <input type="number" v-model="user_id" />
    <button @click="get_info">Get user information</button>
    <p style="color: red">{{ user_info }}</p>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
  },
  data() {
    return {
      user_info: null,
      user_id: 0
    }
  },
  methods: {
    get_info() {
      fetch('http://localhost:5000/user/' + this.user_id).then(
        response => {
          if(response.ok) {
            response.json().then(
              data => this.user_info = data
            )
          } else {
            this.user_info = "User not found"
          }
        }
      ).catch(
        error => console.error(error)
      )
    }
  }
}
</script>

<style scoped>
</style>
