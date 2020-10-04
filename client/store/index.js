export const state = () => ({
  login: false,
  token: "",
});

export const mutations = {
  login(state, token) {
    state.login = true;
    state.token = token;
  },
  logout(state) {
    state.login = false;
    state.token = "";
  },
};
