/* eslint-disable */
export const state = () => ({
  user: {
    username: '',
    email: '',
    id: '',
  },
  token: null,
  status: '',
})

export const mutations = {
  setUser(state, user) {
    state.user = user
  },
  setToken(state, token) {
    state.token = token;
  }

}

export const actions = {
  async signUp(ctx, credentials) {
    return this.$axios
      .post('http://localhost:8000/auth/users/', credentials)
      .then((response) => {
        console.log('signed up')
        console.log(response.data)
        alert('Your account has been created. You will be signed in automatically')
        ctx.dispatch('signIn', credentials)
      })
      .catch((error) => {
        console.log(error.response)
        alert(error.response.request.response)
      })
  },

  async signIn(ctx, credentials) {
    return this.$axios
        .post('http://localhost:8000/auth/token/login/', credentials)
        .then(async (response) => {
          console.log('signed in')
          console.log(response.data)

          ctx.dispatch('setAuthHeader', response.data.auth_token);
          ctx.commit('setToken', response.data.auth_token);
          await ctx.dispatch('fetchUser')
          
          console.log('fetched, pushing')
          this.$router.push('/main')
        })
        .catch((error) => {
          console.log(error.response)
          alert(error.response.request.response)
        })
  },
  async fetchUser(ctx) {
    return this.$axios
      .get('http://localhost:8000/auth/users/me/')
      .then((response) => {
        console.log('fetch user start')
        console.log(response.data)

        let user = {
          username: response.data.username,
          id: response.data.id,
          email: response.data.email,
        }
        ctx.commit('setUser', user)

        console.log('fetch user stop')
      })
      .catch((error) => {
        console.log(error.response)
        alert(error.response.request.response)
      })
  },
  logOut(ctx) {
    ctx.commit('setUser', {})
    ctx.commit('setToken', null)

    this.$router.push('/')
  },

  setAuthHeader(ctx, token) {
    this.$axios.setToken(token, 'Token ');
    console.log('setted in axios');
  },

  middlewareAuthMain(ctx) {
    if (ctx.state.token === null || ctx.state.token === '') {
      this.$router.push('/')
    }
  },
  middlewareAuthSign(ctx) {
    if (ctx.state.token !== null && ctx.state.token !== '') {
      this.$router.push('/main')
    }
  }

}

export const getters = {
  getUser(state) {
    return state.user;
  },
  getToken(state) {
    return state.token;
  }
}