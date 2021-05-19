import { GetStaticProps, GetStaticPaths, NextPage } from 'next'
import Head from 'next/head'
import Link from 'next/link'

import { Container, Typography, Card, CardContent } from '@material-ui/core'

import { Translation, Project } from '../../../src/global.types'
import { getProject, getProjects } from '../../../src/api/projects'
import { getTranslations } from '../../../src/api/translations'

/**
 * Translations Page - Page for viewing and editing translations
 */

interface StaticProps {
  project: Project,
  translations: Translation[],
  englishTranslations: Translation[]
}

export const getStaticPaths: GetStaticPaths = async () => {
  const projects = await getProjects()

  const paths = projects.reduce((acc, project) => {
    return [...acc, ...project.languages.map(language => `/projects/${project.id}/${language.language_code}`)]
  }, [])

  return {
    paths,
    fallback: true,
  }
}

export const getStaticProps: GetStaticProps<StaticProps, {id: string, language_code: string}> = async ({
  params,
}) => {
  const project = await getProject(params.id)
  const selectedLanguage = project.languages.find(language => language.language_code = params.language_code)
  const english = project.languages.find(language => language.language_code = 'en')
  const translations = await getTranslations(parseInt(params.id), selectedLanguage.id)
  const englishTranslations = await getTranslations(parseInt(params.id), english.id)

  return { props: { project, translations, englishTranslations } }
}

const ProjectPage: NextPage<StaticProps> = ({ translations, englishTranslations }) => {
  console.log(englishTranslations)
  return (
    <div>
      <Head>
        <title>Zetkin Translators Interface</title>
        <meta
          name="description"
          content="Contribute to the localisation of Zetkin's software"
        />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main>
        <Container>
          <div style={{
            display: 'grid',
            gridTemplateColumns: '1fr 1fr',
            gridTemplateRows: 'auto'
          }}>
            <div></div>
          </div>          
        </Container>
      </main>
    </div>
  )
}

export default ProjectPage
