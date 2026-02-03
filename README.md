# agriculture-devops-project

## 📁 Project Structure

The repository is organized following best practices for Kubernetes-based microservices and GitOps workflows:

```bash
.
├── k8s/                         # Kubernetes manifests (The "Source of Truth")
│   ├── deployment.yaml          # Application deployment & pod configuration
│   ├── service.yaml             # ClusterIP service for internal networking
│   ├── servicemonitor.yaml      # Prometheus operator config for metrics scraping
│   ├── configmap.yaml           # Grafana dashboard JSON configuration
│   └── namespace.yaml           # Namespace definitions (argocd, default)
├── monitoring/                  # Monitoring stack configuration (Loki/Prometheus)
│   └── values.yaml              # Helm values for loki-stack customization
├── scripts/                     # Operational and testing utilities
│   └── load-generator.ps1       # PowerShell script for manual stress testing
├── app/                         # Application source code
│   ├── main.py                  # Microservice logic with Prometheus metrics
│   └── Dockerfile               # Container definition for the agriculture-app
└── README.md                    # Project documentation and portfolio showcase

```

### Component Descriptions:

* **`/k8s`**: Contains all declarative YAML files that **ArgoCD** monitors to maintain the cluster's desired state.
* **`servicemonitor.yaml`**: A critical DevOps component that allows Prometheus to auto-discover the application's metrics endpoint.
* **`configmap.yaml`**: Stores the Grafana dashboard JSON, allowing the dashboard to be deployed as code (Dashboard-as-Code).
* **`load-generator.ps1`**: Used for the final validation phase to ensure metrics and logs are correctly flowing to the observability stack.

---

## 🏗 Logical Architecture Diagram

To better understand how these files interact within the cluster:

1. **GitHub** stores the manifests.
2. **ArgoCD** pulls the manifests and applies them to **Kubernetes**.
3. **Promtail** and **Prometheus** collect data from the running **Pods**.
4. **Grafana** visualizes this data by querying **Loki** and **Prometheus**.

<img width="2559" height="1425" alt="image" src="https://github.com/user-attachments/assets/be0d34d8-e0c7-4821-9d59-707455178e63" />

### **Grafana Monitoring Hub**

> **Description:** This is the primary interface of the **Grafana Observability Stack** implemented for the Agricultural Platform. The sidebar displays a comprehensive list of pre-configured and custom-built dashboards, including the **Agricultural Platform - Executive View V2**, which serves as the central command center for both business and technical metrics.

**Key features visible in this view:**

* **Centralized Access:** Quick navigation to infrastructure health dashboards like *Node Exporter Full* and *Kubernetes / Views / Pods*.
* **Dashboard-as-Code:** The *Agricultural Platform* dashboard was deployed via a Kubernetes `ConfigMap`, ensuring the monitoring configuration is versioned and reproducible.
* **Operational Readiness:** The "Welcome to Grafana" status confirms that the data sources (Prometheus and Loki) are successfully integrated and ready for real-time data visualization.
<img width="1536" height="1024" alt="7826b2a0-a011-4b81-aadd-6d1e203c501b" src="https://github.com/user-attachments/assets/52a67cb7-1937-41ad-adc7-3a80157e8cba" />



### **Integrated Observability Dashboard: Executive View**

> **Description:** This dashboard provides a comprehensive "single pane of glass" view into the **Agricultural Platform's** health and business operations. It integrates three critical observability dimensions: real-time business metrics, infrastructure traffic, and granular application logs.

**Key Monitoring Components:**

* **Business Logic Tracking (Scenario 1):** The "Products Updated Daily" panel monitors the core functional output of the microservices, tracking successful transaction completions across the cluster.
* **Real-time Traffic Analysis:** The "Real-time System Load" time-series graph visualizes incoming HTTP request rates, allowing for immediate identification of traffic spikes or potential bottlenecks.
* **Log Streaming (Scenario 5):** The "Application Logs" section provides a live feed of microservice activities. As shown in the view, it captures detailed HTTP status codes (e.g., 404 monitoring) and endpoint hits, which is essential for rapid debugging and security auditing.

<img width="1000" height="400" alt="5e153914-0305-4b15-9562-21fe5392b06c" src="https://github.com/user-attachments/assets/cc8e4228-60bf-497d-a105-f68c4636d99b" />

### **Integrated Observability Dashboard: Executive & Infrastructure View**

> **Description:** This dashboard provides a comprehensive "single pane of glass" view into both the **Agricultural Platform's** business operations and the underlying Kubernetes infrastructure health. It integrates critical observability dimensions: real-time business metrics, granular application logs, and global resource utilization.

**Key Monitoring Components:**

* **Business Logic Tracking (Scenario 1):** The "Products Updated Daily" panel monitors the core functional output of the microservices, tracking successful transaction completions across the cluster.
* **Real-time Traffic & System Load:** The "Real-time System Load" time-series graph visualizes incoming HTTP request rates, allowing for immediate identification of traffic spikes or potential bottlenecks.
* **Log Streaming (Scenario 5):** The "Application Logs" section provides a live feed of microservice activities. It captures detailed HTTP status codes and endpoint hits, essential for rapid debugging and security auditing.
* **Global Resource Infrastructure:** The "Kubernetes Resource Count" and "Global CPU/RAM Usage" panels provide a high-level overview of the cluster's health, displaying real-time consumption against defined requests and limits for all 26 running pods.

<img width="2533" height="356" alt="image" src="https://github.com/user-attachments/assets/6b68da4b-2570-40d2-bb33-8cb3f95b9c11" />

### **Infrastructure Health & Resource Utilization Dashboard**

> **Description:** This dashboard provides a high-level overview of the global Kubernetes infrastructure supporting the **Agricultural Platform**. It visualizes critical resource consumption metrics and cluster-wide object counts to ensure the underlying environment is optimized and stable.

**Key Monitoring Components:**

* **Global Resource Analysis:** The dashboard tracks real-time **CPU Utilization** (2.66%) and **RAM Usage** (20.01%) across the entire cluster. It compares "Real" usage against "Requests" and "Limits," which is vital for effective capacity planning and cost optimization.
* **Cluster Object Inventory:** The "Kubernetes Resource Count" panel provides a breakdown of all active resources, including 37 ConfigMaps, 21 Services, and 12 Deployments, ensuring all architectural components are correctly initialized.
* **Workload Monitoring:** The system tracks the operational status of **26 Running Pods** across 5 Namespaces, providing an immediate health check of the distributed microservices.
* **Performance Trends:** Time-series graphs for **Cluster CPU and Memory Utilization** (image_805557) allow for the identification of historical usage patterns and potential resource leaks over time.


<img width="2546" height="346" alt="image" src="https://github.com/user-attachments/assets/fba5cab3-4273-48cb-988a-c6e20000b9d6" />

### **Cluster-Wide Resource & Health Monitoring**

> **Description:** This comprehensive dashboard provides a holistic view of the **Kubernetes Cluster** health, tracking global resource utilization and object distribution. It ensures that the underlying infrastructure for the Agricultural Platform is running within its defined resource boundaries.

**Key Monitoring Insights:**

* **Real-time Resource Utilization:** The dashboard tracks **Global CPU Usage** (currently at 2.66%) and **Global RAM Usage** (20.01%). It visualizes "Real" consumption against "Requests" (1.51%) and "Limits" (2.15%), which is critical for preventing **OOMKilled** (Out of Memory) errors and optimizing cloud costs.
* **Kubernetes Inventory Tracking:** The "Resource Count" panel provides a live inventory of cluster objects, showing 37 ConfigMaps, 21 Services, and 12 Deployments. This ensures all microservice components are correctly declared and initialized by **ArgoCD**.
* **Workload Status:** The system monitors **26 Running Pods** across 5 Namespaces, providing an immediate snapshot of the platform's distribution and availability.
* **Utilization Trends:** High-resolution time-series graphs for **Cluster CPU and Memory Utilization** (image_805557) allow for the identification of historical usage patterns, helping DevOps engineers distinguish between normal operational spikes and potential resource leaks.

<img width="2536" height="390" alt="image" src="https://github.com/user-attachments/assets/354af8ef-a091-44bc-920f-04ed54d76bf5" />

### **Kubernetes Cluster Resource & QoS Monitoring**

> **Description:** This high-level infrastructure dashboard provides deep insights into the resource allocation and health of the entire **Kubernetes Cluster**. It tracks how the Agricultural Platform's microservices utilize the underlying compute resources relative to their defined Quality of Service (QoS) classes.

**Key Infrastructure Insights:**

* **QoS Class Distribution:** The "Kubernetes Pods QoS Classes" panel visualizes the cluster's workload reliability. It shows **26 Total Pods**, with a mix of **BestEffort** (20 pods) and **Burstable** (6 pods) classes, ensuring a balanced distribution between high-performance and flexible workloads.
* **Advanced Resource Planning:** The dashboard tracks **Global RAM Usage** (20.01%) and **Global CPU Usage** (2.66%). By comparing "Real" usage against "Requests" and "Limits" (240 MiB vs 340 MiB), the system ensures the cluster is protected against resource contention while maintaining high efficiency.
* **Pod Health & Status Analysis:** The "Kubernetes Pods Status Reason" panel monitors for critical cluster events like Evictions, NodeLost, or Shutdowns. The current zero-value status confirms a stable and healthy environment.
* **Cluster-wide Object Inventory:** A live count of all active Kubernetes objects (37 ConfigMaps, 21 Services, 12 Deployments) ensures complete architectural parity with the manifests stored in GitHub and deployed via **ArgoCD**.

<img width="2539" height="1039" alt="image" src="https://github.com/user-attachments/assets/a7f87c11-095e-418d-88f0-b5285fa09b10" />

### **Network Performance & Bandwidth Utilization Analysis**

> **Description:** This specialized dashboard monitors the global and instance-level network performance of the **Kubernetes Cluster**. It provides critical data on bandwidth throughput and network reliability, ensuring that the Agricultural Platform's microservices can communicate with minimal latency.

**Key Network Metrics:**

* **Global Network Throughput:** The "Global Network Utilization by device" panel tracks real-time data transfer rates across the cluster, showing bidirectional traffic (Inbound/Outbound) reaching peaks of **256 KiB/s**.
* **Instance-Level Connectivity:** Detailed breakdown panels like "Network Received by instance" allow for granular monitoring of traffic distribution between different pods and services.
* **Reliability & Saturation:** The "Network Saturation - Packets dropped" panel is a critical health indicator. The current zero-value across the timeline confirms that the network buffer is not saturated and no data loss is occurring between services.
* **Virtual Device Traffic:** The "Total Network Received (with all virtual devices)" panel visualizes the total traffic handled by the Kubernetes virtual networking layer (veth pairs), ensuring the container network interface (CNI) is operating efficiently.

<img width="2544" height="1038" alt="image" src="https://github.com/user-attachments/assets/fbe42e30-abf1-465c-a1f0-ddd1172b2a5b" />


### **Comprehensive Node Infrastructure & Performance Analytics**

> **Description:** This detailed dashboard monitors the fundamental compute, memory, and network resources of the **Kubernetes Node** supporting the Agricultural Platform. It provides deep visibility into kernel-level operations and hardware resource saturation, ensuring the underlying host is performing optimally.

**Key Infrastructure Insights:**

* **CPU Operational Breakdown:** The dashboard tracks CPU utilization by mode, distinguishing between **System** (kernel mode), **User** (application mode), and **Iowait**. Monitoring these sub-metrics is essential for identifying whether performance bottlenecks are caused by application logic or system-level overhead.
* **Advanced Memory Allocation:** Beyond simple usage, this panel tracks memory distribution across **User-space applications**, **PageTables**, and **Kernel Caches**. Tracking the `Cache` and `SwapCache` metrics (averaging ~3.50 GiB) ensures the system effectively manages file content caching to minimize disk I/O latency.
* **Interface-Level Network Traffic:** The "Network Traffic" panel monitors bidirectional data flow across specific interfaces like `eth0`, `docker0`, and `veth` pairs. Peak rates of **1.52 Mb/s** on `eth0` demonstrate the node's ability to handle high-volume inter-pod and external communication.
* **System Saturation Monitoring:** The "Network Saturation" metric tracks micro-level packet drops and errors across all virtual and physical devices. The stable, near-zero values confirm a clean network path with no significant congestion or hardware-level errors.

<img width="2559" height="859" alt="image" src="https://github.com/user-attachments/assets/dca1395c-2515-423c-b23e-a239f62afb43" />

### **Comprehensive Node Health & Resource Utilization Overview**

> **Description:** This high-level dashboard provides a mission-critical summary of the **Kubernetes Node's** health, focusing on the four primary pillars of infrastructure: CPU, Memory, Network, and Disk. It allows for rapid assessment of system "pressure" and resource saturation, ensuring the host environment can support the Agricultural Platform's microservices.

**Key Monitoring Insights:**

* **Instant Resource Gauges:** The dashboard provides real-time gauges for **CPU Busy** (3.3%) and **RAM Used** (20.5%). These indicators offer an immediate "at-a-glance" status check of the physical or virtual host's health.
* **System Pressure Analysis:** Using the **Pressure** panel, the system monitors for resource contention across CPU, Memory, and I/O. Current low values (0.3% CPU pressure) confirm that the microservices are not waiting for hardware availability.
* **Historical Infrastructure Trends:** Detailed time-series graphs for **CPU Basic** and **Memory Basic** track resource consumption over a 24-hour period. This historical data is essential for identifying daily operational cycles and long-term infrastructure trends.
* **Storage & Network Integrity:** The dashboard monitors bidirectional **Network Traffic** and **Disk Space Usage** across multiple mount points. Tracking disk utilization across partitions like `/mnt/host/wsl/docker-desktop` ensures that log accumulation or data persistence does not lead to unexpected system failure.

<img width="2544" height="700" alt="image" src="https://github.com/user-attachments/assets/eb7ff771-8c3b-4b5c-84d7-6b729f0dd91d" />

### **Deep Infrastructure Observability & System Metrics**

> **Description:** To ensure the maximum reliability of the Agricultural Platform, a comprehensive node-level monitoring system was implemented using **Prometheus Node Exporter**. This stack provides granular visibility into the underlying Linux host and Kubernetes worker nodes across multiple operational layers.

**Monitored System Layers:**

* **Compute & Memory Intelligence:** Real-time tracking of CPU operational modes (User, System, Iowait) and detailed memory distribution (Apps, Cache, PageTables), ensuring optimal resource allocation and preventing system bottlenecks.
* **Network & Connectivity:** Comprehensive monitoring of network traffic basics, socket statuses, and netstat analytics. This allows for precise detection of packet loss, latency spikes, and unauthorized connection attempts.
* **Storage & Filesystem Health:** Automated tracking of disk I/O performance and filesystem capacity across all partitions, preventing application failures due to storage exhaustion.
* **System Operations (Systemd & Processes):** Monitoring of core OS services and process lifecycles to ensure that the container runtime and orchestration agents are operating without interruption.

### **GitOps Continuous Deployment with ArgoCD**

#### **1. Application Sync Status**

> **Description:** This view confirms the successful implementation of **GitOps** using ArgoCD. The "Healthy" and "Synced" status indicates that the live state of the Kubernetes cluster perfectly matches the declarative configuration defined in the GitHub repository.

* **Target Revision:** The system is tracking the `HEAD` of the repository, ensuring that every commit to the `k8s/` path is automatically reflected in the cluster.
* **Automated Governance:** The last synchronization occurred recently, proving that the automated deployment pipeline is active and responsive.
<img width="500" height="500" alt="ChatGPT Image 25 янв  2026 г , 23_57_22" src="https://github.com/user-attachments/assets/667dfe49-aaf1-4fb6-88c5-75f3b8bf6ea9" />



#### **2. Visual Infrastructure Topology**

> **Description:** ArgoCD provides a real-time graph of the **Agricultural Platform's** architectural components within the Kubernetes namespace. This tree view visualizes the logical relationship between the parent application and its child resources.

* **Resource Hierarchy:** The diagram shows the `agriculture-app` Deployment managing multiple **ReplicaSets**, which in turn manage the lifecycle of the active **Pods**.
* **Service Discovery & Config:** The presence of `agriculture-app-service` (svc) and `agri-dashboard-config` (cm) confirms that network routing and dashboard-as-code configurations are correctly provisioned.
* **Observability Integration:** The `agriculture-app-monitor` (ServiceMonitor) is successfully deployed, enabling **Prometheus** to automatically discover and scrape application-level metrics.

<img width="1717" height="521" alt="image" src="https://github.com/user-attachments/assets/f43c66b9-abcc-4b7b-bd80-fcc6d2f3953d" />


---


## 🔮 Future Enhancements

While the current infrastructure provides a solid foundation for the Agricultural Platform, the following improvements are planned to further align with industry-leading DevOps practices:

* **Alerting Integration:** Implementing **Alertmanager** to send real-time notifications via Slack or Email when critical thresholds (e.g., CPU > 80% or Pod Restarts) are reached.
* **Auto-scaling (HPA):** Configuring **Horizontal Pod Autoscaler** to automatically increase the number of `agriculture-app` replicas during peak traffic periods detected on the Grafana traffic dashboard.
* **CI/CD Pipeline Security:** Integrating **SonarQube** and **Snyk** for automated security scanning of Docker images and Python code before deployment by ArgoCD.
* **Persistent Storage:** Transitioning from stateless pods to stateful workloads using **Persistent Volume Claims (PVC)** for better data durability in the message broker layer (Kafka/RabbitMQ).

## 📝 Conclusion

This project successfully demonstrates the deployment of a highly available, observable, and automated infrastructure for a modern microservices application. By leveraging **Kubernetes** for orchestration, **ArgoCD** for GitOps-driven deployment, and a full **Prometheus-Loki-Grafana** stack for observability, the platform achieves a professional level of reliability and maintainability. The diagnostic and testing phases conducted during development ensure that the system is ready for production-level traffic and operational challenges.



