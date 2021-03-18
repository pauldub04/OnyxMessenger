/* eslint-disable */
export const state = () => ({
  user: null,
})

export const mutations = {
  setUser(state, user) {
    state.user = user
  },
}

export const actions = {
  fetchUser(ctx) {
    this.$axios
      .get('http://localhost:8000/auth/users/me/', {
        headers: {
          "Authorization": 'Token ' + sessionStorage.getItem('authToken')
        }
      })
      .then((response) => {
        console.log('fetch user')
        console.log(response.data)

        sessionStorage.setItem('username', response.data.username)
        sessionStorage.setItem('id', response.data.id)
        sessionStorage.setItem('email', response.data.email)

        ctx.commit('setUser', response.data)
      })
      .catch((error) => {
        console.log(error.response)
        alert(error.response.request.response)
      })
  },
  logOut(ctx) {
    sessionStorage.setItem('authToken', null)
    ctx.commit('setUser', {})
    this.$router.push('/auth')
  },

}

export const getters = {}