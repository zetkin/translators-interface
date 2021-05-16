import fetchWrapper from './fetchWrapper'

export const getProjects = async () => {
  return fetchWrapper({ url: 'http://localhost:8000/projects/' })
}

export const getProject = async (projectId) => {
  return fetchWrapper({ url: `http://localhost:8000/projects/${projectId}/` })
}
