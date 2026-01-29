# Business Operations Standard Operating Procedures

## 1. Task Follow-up Guidelines

### 1.1 Follow-up Frequency
- **Active Tasks (In Progress)**: Follow-up every 3 business days
- **Pending Tasks**: Follow-up every 5 business days
- **Overdue Tasks**: Immediate follow-up required, escalate if >7 days overdue

### 1.2 Follow-up Protocol
When a task requires follow-up:
1. Check last follow-up date
2. If no follow-up in past 3 days (active) or 5 days (pending), trigger reminder
3. Include task details: client name, owner, status, due date
4. CC project manager if task is overdue

### 1.3 Overdue Task Escalation
- **1-3 days overdue**: Send reminder to task owner
- **4-7 days overdue**: Send reminder + CC team lead
- **8+ days overdue**: Escalate to senior management with action plan request

### 1.4 Missing Information Handling
- If task owner is missing: Assign to default project manager
- If due date is missing: Request clarification from task creator
- If last follow-up is missing: Assume no prior follow-up, trigger immediately

---

## 2. Weekly Reporting Cadence

### 2.1 Report Generation Schedule
- **Frequency**: Every Monday at 9:00 AM
- **Coverage Period**: Previous 7 days (Monday to Sunday)
- **Distribution**: All team leads + operations manager

### 2.2 Required Metrics

#### Task Metrics
- Total active tasks
- Tasks completed this week
- Overdue tasks (count + % of total)
- Average task completion time
- Top 3 clients by task volume

#### Sales Metrics
- Total pipeline value
- New leads created this week
- Deals closed (count + total value)
- Conversion rate (closed won / total leads)
- Average deal size

### 2.3 Report Format
Reports must be:
- **Structured**: JSON format for downstream integration
- **Timestamped**: Include generation date/time
- **Actionable**: Highlight items requiring attention
- **Comparable**: Use consistent metrics week-over-week

---

## 3. Business Insights & Decision Support

### 3.1 Data Sources
Insights must be grounded in:
- Current task tracker data (tasks.csv)
- Sales pipeline data (sales.csv)
- Historical trends (when available)
- This SOP document for business rules

### 3.2 Insight Quality Standards
- **Factual**: All claims must reference specific data points
- **Contextual**: Explain "why" using business logic
- **Actionable**: Provide clear next steps
- **Risk-aware**: Flag potential issues proactively

### 3.3 Common Insight Requests
- "Why are tasks overdue for [client]?"
- "What's blocking progress on [project]?"
- "Should we escalate [task/deal]?"
- "What's our team capacity this week?"

### 3.4 Handling Ambiguity
If data is insufficient:
1. State what is known
2. List missing information
3. Recommend data collection steps
4. Provide conditional recommendations

---

## 4. Data Quality Requirements

### 4.1 Mandatory Fields
**Tasks**: task_id, client, owner, status, due_date  
**Sales**: lead_id, client, stage, value, created_date

### 4.2 Validation Rules
- Dates must be in YYYY-MM-DD format
- Status must be one of: Pending, In Progress, Completed, Overdue
- Sales stages: Initial Contact, Discovery, Proposal Sent, Negotiation, Closed Won, Closed Lost
- Values must be numeric (USD)

### 4.3 Error Handling
- Missing non-critical fields: Flag in report, continue processing
- Invalid date formats: Reject row, log error
- Duplicate IDs: Use first occurrence, warn user

---

## 5. Automation Principles

### 5.1 Human-in-the-Loop
Automation should:
- **Recommend**, not decide
- **Flag** edge cases for human review
- **Explain** its reasoning
- **Preserve** audit trails

### 5.2 Fail-Safe Defaults
- If uncertain: Ask for clarification
- If data missing: Use conservative estimates
- If rules conflict: Escalate to manual review

### 5.3 Continuous Improvement
- Log all automation decisions
- Review monthly for accuracy
- Update rules based on feedback

---

## Document Version
**Version**: 2.1  
**Last Updated**: January 15, 2026  
**Owner**: Operations Team  
**Review Cycle**: Quarterly