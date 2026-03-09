# RELATÓRIO DE IMPLEMENTAÇÃO DE SERVIÇOS AWS

**Data:** 09 de marco de 2026  
**Empresa:** Abstergo Industries  
**Responsável:** Ramon Azevedo  
**Departamento:** Tecnologia da Informação  
**Projeto:** Otimização de Custos Operacionais com AWS

---

## Introdução

Este relatório apresenta o processo de implementação de ferramentas na empresa Abstergo Industries, realizado por Ramon Azevedo. O objetivo do projeto foi elencar 3 serviços AWS, com a finalidade de realizar diminuição de custos imediatos na operação farmacêutica, mantendo a qualidade dos serviços e a conformidade regulatória.

---

## Descrição do Projeto

O projeto de implementação de ferramentas foi dividido em 3 etapas, cada uma com seus objetivos específicos. A seguir, serão descritas as etapas do projeto:

### Etapa 1: Amazon EC2 com Auto Scaling
- **Nome da ferramenta:** Amazon EC2 (Elastic Compute Cloud) com Auto Scaling Groups
- **Foco da ferramenta:** Otimização de recursos computacionais e redução de custos com infraestrutura
- **Descrição de caso de uso:** Implementação de instâncias EC2 dimensionadas adequadamente para o sistema de gestão farmacêutica, substituindo servidores físicos superdimensionados. O Auto Scaling permite ajustar automaticamente a capacidade computacional conforme a demanda, reduzindo custos em horários de baixo movimento (madrugadas e finais de semana) e garantindo performance nos horários de pico. Estimativa de redução de 40% nos custos de infraestrutura.

### Etapa 2: Amazon RDS com Reserved Instances
- **Nome da ferramenta:** Amazon RDS (Relational Database Service) com Reserved Instances
- **Foco da ferramenta:** Gerenciamento otimizado de banco de dados e redução de custos operacionais
- **Descrição de caso de uso:** Migração do banco de dados de prescrições, estoque e controle de medicamentos para Amazon RDS, eliminando custos com licenciamento, manutenção e administração de banco de dados on-premises. A contratação de Reserved Instances para 1 ano proporciona desconto de até 40% comparado ao modelo on-demand. Backups automatizados e alta disponibilidade garantem conformidade com regulamentações da ANVISA.

### Etapa 3: Amazon S3 com Intelligent-Tiering
- **Nome da ferramenta:** Amazon S3 (Simple Storage Service) com Intelligent-Tiering
- **Foco da ferramenta:** Armazenamento inteligente e econômico de documentos e arquivos
- **Descrição de caso de uso:** Armazenamento de receitas digitalizadas, laudos médicos, notas fiscais e documentos regulatórios no Amazon S3 com a classe Intelligent-Tiering, que move automaticamente os dados entre camadas de acesso conforme padrões de uso. Documentos recentes permanecem em acesso frequente, enquanto arquivos antigos migram para camadas mais econômicas. Redução estimada de 70% nos custos de armazenamento comparado a soluções tradicionais, com conformidade LGPD através de criptografia e controles de acesso.

---E
## Resultados Esperados

### Benefícios Financeiros
- **Redução de custos operacionais:** Estimativa de economia de 45% nos custos de TI no primeiro ano
- **Eliminação de CAPEX:** Conversão de investimentos em infraestrutura para modelo OPEX previsível
- **Otimização de recursos:** Pagamento apenas pelos recursos efetivamente utilizados

### Benefícios Operacionais
- **Escalabilidade:** Capacidade de crescimento sem investimentos antecipados em infraestrutura
- **Alta disponibilidade:** SLA de 99.99% garantindo continuidade do negócio
- **Segurança aprimorada:** Conformidade com LGPD, ANVISA e padrões internacionais
- **Backup automatizado:** Proteção de dados críticos sem intervenção manual

### Benefícios Estratégicos
- **Agilidade:** Implementação de novos serviços em minutos ao invés de semanas
- **Foco no core business:** Equipe de TI dedicada a inovação ao invés de manutenção de infraestrutura
- **Modernização tecnológica:** Base sólida para futuras implementações de IA e analytics

---

## Conclusão

A implementação de ferramentas na empresa Abstergo Industries tem como esperado a redução significativa de custos operacionais, aumento da eficiência tecnológica e melhoria na qualidade dos serviços prestados, o que aumentará a eficiência e a produtividade da empresa. 

Os três serviços AWS selecionados (EC2 com Auto Scaling, RDS com Reserved Instances e S3 com Intelligent-Tiering) foram escolhidos estrategicamente para atender às necessidades específicas do setor farmacêutico, garantindo conformidade regulatória, segurança de dados e otimização de custos.

Recomenda-se a continuidade da utilização das ferramentas implementadas, monitoramento constante através do AWS Cost Explorer para identificação de novas oportunidades de otimização, e a busca por novas tecnologias que possam melhorar ainda mais os processos da empresa, como AWS Lambda para automações e Amazon CloudWatch para monitoramento proativo.

---

## Anexos

1. [Planilha comparativa de custos: On-Premises vs AWS]()
2. [Arquitetura técnica detalhada da solução implementada]()
3. [Cronograma de migração e implementação]()
4. [Documentação de conformidade regulatória (ANVISA/LGPD)]()
5. [Manual de operação e melhores práticas AWS]()
6. [Plano de disaster recovery e continuidade de negócios]()
7. [Relatório de análise de ROI (Return on Investment)]()

---

**Assinatura do Responsável pelo Projeto:**

Ramon Azevedo  
Gerente de Projetos de TI  
Abstergo Industries

---