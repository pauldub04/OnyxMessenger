export default function ({ store, redirect }) {
  console.log('middleware, token = ')
  console.log(store.state.token)
  if (store.state.token === null || store.state.token === '') {
    return redirect('/login')
  }
}
