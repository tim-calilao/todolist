{% load static %}
{% load render_table from django_tables2 %}
{% load table_tags %}
<!DOCTYPE html>
<html lang="en" style="overflow-x:hidden;">

<head>

    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="description" content="">
    <meta name="author" content="">

    <title>To-do List Management</title>

    <!-- DataTables CSS -->
    <!-- <link href="{% static '/css/dataTables.bootstrap' %}" rel="stylesheet"> -->

    <!-- Bootstrap Core CSS -->
    <link href="{% static '/css/bootstrap.min.css' %}" rel="stylesheet">

    <!-- Custom CSS -->
    <link href="{% static '/css/sb-admin.css' %}" rel="stylesheet">

    <!-- Morris Charts CSS -->
    <link href="{% static '/css/plugins/morris.css' %}" rel="stylesheet">

    <script src = "{% static '/js/jquery-3.1.1.js' %}"></script>

    <!-- Custom Fonts -->
    <link href="{% static '/font-awesome/css/font-awesome.min.css' %}" rel="stylesheet" type="text/css">

    <!-- HTML5 Shim and Respond.js IE8 support of HTML5 elements and media queries -->
    <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
    <!--[if lt IE 9]>
        <script src="https://oss.maxcdn.com/libs/html5shiv/3.7.0/html5shiv.js"></script>
        <script src="https://oss.maxcdn.com/libs/respond.js/1.4.2/respond.min.js"></script>
    <![endif]-->

</head>

<body>

    <div id="wrapper">

        <!-- Navigation -->
        <nav class="navbar navbar-inverse navbar-fixed-top" role="navigation">
            <!-- Brand and toggle get grouped for better mobile display -->
            <div class="navbar-header">
                <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-ex1-collapse">
                    <span class="sr-only">Toggle navigation</span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a class="navbar-brand" href="login.html">To-do List Management</a>
            </div>
            <!-- Top Menu Items -->
            <!-- <ul class="nav navbar-right top-nav">                
                <li class="dropdown">
                    <a href="#" class="dropdown-toggle" data-toggle="dropdown"><i class="fa fa-user"></i> User Name <b class="caret"></b></a>
                    <ul class="dropdown-menu">                        
                        <li>
                            <a href="#"><i class="fa fa-fw fa-gear"></i> Settings</a>
                        </li>
                        <li class="divider"></li>
                        <li>
                            <a href="#"><i class="fa fa-fw fa-power-off"></i> Log Out</a>
                        </li>
                    </ul>
                </li>
            </ul> -->
            <!-- Sidebar Menu Items - These collapse to the responsive navigation menu on small screens -->
            <div class="collapse navbar-collapse navbar-ex1-collapse">
                <ul class="nav navbar-nav side-nav">
                    <li>
                        <a href="index.php"><i class="fa fa-fw fa-dashboard"></i> Home</a>
                    </li>
                    <li class="active">
                        <a href="tables.php"><i class="fa fa-fw fa-calendar"></i> To-do List</a>
                    </li>
                    <li>
                        <a href=""><i class="fa fa-fw fa-table"></i> To-do List Management</a>
                    </li>
                </ul>
            </div>
        </nav>

        <div id="page-wrapper">

            <div class="container-fluid">
                <!-- Page Heading -->
                <div class="row">
                    <div class="col-lg-12">
                        <h2 class="page-header">
                            To-do List <small></small>
                        </h2>
                        <!-- <ul class="list-group">
                            <li class="list-group-item list-group-item-info"><strong>Legend</strong></li>
                            <li class="list-group-item list-group-item-success">Completed On-Time</li>
                            <li class="list-group-item list-group-item-warning">Near Deadline</li>
                            <li class="list-group-item list-group-item-danger">Exceeded Deadline</li>
                            <li class="list-group-item">Not Completed/Exceeded Deadline</li>
                        </ul> -->
                    </div>
                </div>
                <!-- /.row -->
                {% render_table table%}
                <div class="row">
                    <div class="container">

                        <!-- <table class="table table-striped" style="width:95%">
                            <thead>
                                <tr class="info">
                                    <th>Completed</th>
                                    <th>Activity</th>
                                    <th>Notes</th>
                                    <th>Deadline</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr class="success">
                                    <td><input type="checkbox" checked="true"></td>
                                    <td>Start of Midterm Exams</td>
                                    <td>Focus on Mathematics and Science</td>
                                    <td>5/12/2016 9:00 AM</td>
                                </tr>
                                <tr>
                                    <td><input type="checkbox"</td>
                                    <td>Another long sample text to see what will happen when different columns have very long texts.</td>
                                    <td>Sample Notes</td>
                                    <td>1/1/2020 4:30 PM</td>
                                </tr>
                                <tr>
                                    <td><input type="checkbox"</td>
                                    <td>Sample Activity</td>
                                    <td>A very long sample text to show what will happen when the text is too long but since it is not enough this will continue because I refuse to use Lorem Ipsum.</td>
                                    <td>1/1/2020</td>
                                </tr>
                                <tr class="danger">
                                    <td><input type="checkbox"></td>
                                    <td>Quiz for Professional Ethics</td>
                                    <td>Review Powerpoint #3</td>
                                    <td>7/17/2016 9:00 AM</td>
                                </tr>
                                <tr class="warning">
                                    <td><input type="checkbox" checked="true"></td>
                                    <td>UI Sample for CPA</td>
                                    <td>Just.Do.It</td>
                                    <td>9/27/2016 11:00 AM</td>
                                </tr>
                                <tr>
                                    <td><input type="checkbox"</td>
                                    <td>Sample Activity</td>
                                    <td>Sample Notes</td>
                                    <td> </td>
                                </tr>
                            </tbody>
                        </table> -->
                    </div>
                    <br><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br>
            </div>
            <!-- /.container-fluid -->

        </div>
        <!-- /#page-wrapper -->

    </div>
    <!-- /#wrapper -->

</body>

</html>
