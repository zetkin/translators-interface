import { Project } from '../global.types'
import fetchWrapper from './fetchWrapper'

export const getProjects = async (): Promise<Project[]> => {
  return fetchWrapper({ url: 'http://localhost:8000/projects/' })
}

export const getProject = async (projectId): Promise<Project> => {
  return fetchWrapper({ url: `http://localhost:8000/projects/${projectId}/` })
}
